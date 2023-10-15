# -*- coding: utf-8 -*-

"""
# Language: Python 3
# Written by: Manuel Martinez
# Description: Abstract class for checking if a day is a workday or not.
"""

import json
import os

from abc import ABC, abstractmethod
from datetime import datetime, timedelta


class WorkdayChecker(ABC):
    """Abstract class for checking if a day is a workday or not."""

    @abstractmethod
    def is_workday(self, date: datetime) -> bool:
        """Check if a day is a workday or not.

        Args:
            date (datetime): Date to check.

        Returns:
            bool: True if the date is a workday, False otherwise.
        """


class HolydayChecker(WorkdayChecker):
    """Class for checking if a day is a workday or not."""

    def __init__(self, holydays_file: str = None):
        """Constructor.

        Args:
            holydays_file (str, optional): Path to the file with the holydays.
            Defaults to None.
        """
        self.holydays_file = holydays_file
        self.holydays = self._load_holydays()

    def is_workday(self, date: datetime) -> bool:
        """Check if a day is a workday or not.

        Args:
            date (datetime): Date to check.

        Returns:
            bool: True if the date is a workday, False otherwise.
        """
        return date not in self.holydays

    def _load_holydays(self) -> list:
        """Load the holydays from the file.

        Returns:
            list: List of holydays.
        """
        if self.holydays_file is None:
            return []

        if not os.path.exists(self.holydays_file):
            return []

        with open(self.holydays_file, 'r', encoding='utf-8') as holydays_file:
            holydays = json.load(holydays_file)

        holydays = holydays.get('holydays', [])

        return [
            datetime.strptime(holyday_date, '%Y-%m-%d')
            for holyday_date in holydays
        ]


class VacationChecker(WorkdayChecker):
    """Class for checking if a day is a workday or not."""

    def __init__(self, vacations_file: str = None):
        """Constructor.

        Args:
            vacations_file (str, optional): Path to the file with the
            vacations. Defaults to None.
        """
        self.vacations_file = vacations_file
        self.vacations = self._load_vacations()

    def is_workday(self, date: datetime) -> bool:
        """Check if a day is a workday or not.

        Args:
            date (datetime): Date to check.

        Returns:
            bool: True if the date is a workday, False otherwise.
        """
        return date not in self.vacations

    def _load_vacations(self) -> list:
        """Load the vacations from the file.

        Returns:
            list: List of vacations.
        """
        if self.vacations_file is None:
            return []

        if not os.path.exists(self.vacations_file):
            return []

        with open(self.vacations_file,
                  'r',
                  encoding='utf-8') as vacations_file:
            vacations = json.load(vacations_file)

        vacations = vacations.get('vacations', [])

        vacation_days = []

        for vacation_range in vacations:
            start_date = datetime.strptime(vacation_range['begin'], '%Y-%m-%d')
            end_date = datetime.strptime(vacation_range['end'], '%Y-%m-%d')
            vacation_days += self._get_days_from_range(start_date, end_date)

        return vacation_days

    def _get_days_from_range(
            self,
            start_date: datetime,
            end_date: datetime) -> list:
        """Get the days from a range of dates.

        Args:
            start_date (datetime): Start date of the range.
            end_date (datetime): End date of the range.

        Returns:
            list: List of dates.
        """
        days = []
        while start_date <= end_date:
            days.append(start_date)
            start_date += timedelta(days=1)

        return days


class WeekendChecker(WorkdayChecker):
    """Class for checking if a day is a workday or not."""

    def is_workday(self, date: datetime) -> bool:
        """Check if a day is a workday or not.

        Args:
            date (datetime): Date to check.

        Returns:
            bool: True if the date is a workday, False otherwise.
        """
        return date.weekday() < 5


def is_date_workday(date: datetime) -> bool:
    """Check if a day is a workday or not.

    Args:
        date (datetime): Date to check.
        holydays_file (str, optional): Path to the file with the holydays.
        Defaults to None.
        vacations_file (str, optional): Path to the file with the vacations.
        Defaults to None.

    Returns:
        bool: True if the date is a workday, False otherwise.
    """

    holydays_file_path = os.path.join(
        os.path.dirname(__file__),
        'resources',
        'holydays.json'
    )

    holyday_checker = HolydayChecker(holydays_file_path)
    vacation_checker = VacationChecker(holydays_file_path)
    weekend_checker = WeekendChecker()

    is_date_a_holiday = holyday_checker.is_workday(date)
    is_date_a_vacation = vacation_checker.is_workday(date)
    is_date_a_weekend = weekend_checker.is_workday(date)

    is_workday = not (
        is_date_a_holiday or
        is_date_a_vacation or
        is_date_a_weekend
    )

    if is_workday:
        return True

    return False

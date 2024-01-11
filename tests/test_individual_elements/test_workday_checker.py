# test_workday_checker.py

import os
import unittest
from datetime import datetime
from work_time_logger.workday_checker import (
    HolydayChecker, WeekendChecker, VacationChecker)


class TestHolydayChecker(unittest.TestCase):
    """Test class for the HolydayChecker class."""
    def __init__(self, *args, **kwargs):
        super(TestHolydayChecker, self).__init__(*args, **kwargs)

        test_json_path = os.path.join(
            os.path.dirname(__file__), "resources", "holiday_test.json"
        )

        self.holyday_checker = HolydayChecker(test_json_path)

    def test_holyday_checker_negative(self):
        """Test with an existing holiday"""
        is_workday = self.holyday_checker.is_workday(
            date=datetime(2023, 1, 1)
        )

        self.assertFalse(is_workday)

    def test_holyday_checker_positive(self):
        """Test with a non existing holiday"""
        is_workday = self.holyday_checker.is_workday(
            date=datetime(2023, 1, 2)
        )

        self.assertTrue(is_workday)


class TestVacationChecker(unittest.TestCase):
    """Test class for the VacationChecker class."""
    def __init__(self, *args, **kwargs):
        super(TestVacationChecker, self).__init__(*args, **kwargs)

        test_json_path = os.path.join(
            os.path.dirname(__file__), "resources", "vacation_test.json"
        )

        self.vacation_checker = VacationChecker(test_json_path)

    def test_vacation_checker_negative(self):
        """Test with an existing vacation"""
        is_workday = self.vacation_checker.is_workday(
            date=datetime(2023, 1, 1)
        )

        self.assertFalse(is_workday)

    def test_vacation_checker_positive(self):
        """Test with a non existing vacation"""
        is_workday = self.vacation_checker.is_workday(
            date=datetime(2023, 1, 3)
        )

        self.assertTrue(is_workday)


class TestWeekendChecker(unittest.TestCase):
    """Test class for the WeekendChecker class."""
    def __init__(self, *args, **kwargs):
        super(TestWeekendChecker, self).__init__(*args, **kwargs)

        self.weekend_checker = WeekendChecker()

    def test_weekend_checker_negative(self):
        """Test with a weekend day"""
        is_workday = self.weekend_checker.is_workday(
            date=datetime(2023, 1, 7)
        )

        self.assertFalse(is_workday)

    def test_weekend_checker_positive(self):
        """Test with a non weekend day"""
        is_workday = self.weekend_checker.is_workday(
            date=datetime(2023, 1, 3)
        )

        self.assertTrue(is_workday)

# -*- coding: utf-8 -*-

"""
# Language: Python 3
# Written by: Manuel Martinez
# Description: Selenium script for marking the hours in the workday.
"""


from datetime import datetime
from enum import Enum

from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select

from work_time_logger import config


class ExitCode(Enum):
    """Enum for the exit codes."""

    SUCCESS = 0
    LOGIN_TIMEOUT = 1
    IN_DATE_ERROR = 2
    OUT_DATE_ERROR = 3
    LOGOUT_TIMEOUT = 4
    ALREADY_MARKED = 5


def mark_working_hours(date: datetime):
    """
    Mark the working hours in the web page.
    """

    # Create the options for the browser
    options = ChromeOptions()
    options.add_argument("--headless")

    # Get sensitive data from the config file
    username = config.USERNAME
    password = config.PASSWORD
    website = config.LOGGING_WEBSITE
    place_value = config.PLACE_VALUE

    # logging info from config file
    start_hour = config.START_HOUR
    start_minute = config.START_MINUTE
    end_hour = config.END_HOUR
    end_minute = config.END_MINUTE
    friday_end_hour = config.FRIDAY_END_HOUR
    friday_end_minute = config.FRIDAY_END_MINUTE

    # set the start and end time
    start_time = datetime(
        date.year, date.month, date.day, start_hour, start_minute
    )
    if date.weekday() == 4:
        end_time = datetime(
            date.year,
            date.month,
            date.day,
            friday_end_hour,
            friday_end_minute
        )
    else:
        end_time = datetime(
            date.year,
            date.month,
            date.day,
            end_hour,
            end_minute
        )

    # Create the browser
    browser = webdriver.Chrome(options=options)

    # Go to the web page
    browser.get(website)

    # wait for login form to load
    try:
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.NAME, "ImageButtonEx1"))
        )
    except TimeoutError:
        browser.quit()
        return ExitCode.LOGIN_TIMEOUT

    # Fill the login form
    browser.find_element(By.NAME, "tboxUsuario").send_keys(username)
    browser.find_element(By.NAME, "tboxClave").send_keys(password)
    browser.find_element(By.NAME, "ImageButtonEx1").click()

    # wait for the main page to load
    try:
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.NAME, "imgbtnFichaEntrada"))
        )
    except TimeoutError:
        browser.quit()
        return ExitCode.LOGIN_TIMEOUT

    # Fill the date field
    date_field = browser.find_element(By.NAME, "tboxInicio")
    date_field.clear()
    date_field.send_keys(start_time.strftime("%d/%m/%Y"))

    # Fill the start time field
    hour_field = browser.find_element(By.NAME, "tboxHoraIni")
    hour_field.clear()
    hour_field.send_keys(start_time.strftime("%H:%M"))

    # fill place field
    place_field = Select(browser.find_element(By.NAME, "ddlAreas"))
    place_field.select_by_value(place_value)

    # submit the form
    browser.find_element(By.NAME, "imgbtnFichaEntrada").click()

    # wait for the confirmation page to load
    try:
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.NAME, "imgbtnVolver"))
        )
    except TimeoutError:
        browser.quit()
        return ExitCode.IN_DATE_ERROR

    # click the confirmation button
    browser.find_element(By.NAME, "imgbtnVolver").click()

    # wait for the main page to load
    try:
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.NAME, "imgbtnFichaSalida"))
        )
    except TimeoutError:
        browser.quit()
        return ExitCode.IN_DATE_ERROR

    # Fill the date field
    date_field = browser.find_element(By.NAME, "tboxInicio")
    date_field.clear()
    date_field.send_keys(end_time.strftime("%d/%m/%Y"))

    # Fill the start time field
    hour_field = browser.find_element(By.NAME, "tboxHoraIni")
    hour_field.clear()
    hour_field.send_keys(end_time.strftime("%H:%M"))

    # fill place field
    place_field = Select(browser.find_element(By.NAME, "ddlAreas"))
    place_field.select_by_value(place_value)

    # submit the form
    browser.find_element(By.NAME, "imgbtnFichaSalida").click()

    # wait for the confirmation page to load
    try:
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.NAME, "imgbtnVolver"))
        )
    except TimeoutError:
        browser.quit()
        return ExitCode.OUT_DATE_ERROR

    # click the confirmation button
    browser.find_element(By.NAME, "imgbtnVolver").click()

    # wait for the exit button to load
    try:
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.NAME, "ImageButtonEx1"))
        )
    except TimeoutError:
        browser.quit()
        return ExitCode.OUT_DATE_ERROR

    # click the exit button
    browser.find_element(By.NAME, "ImageButtonEx1").click()

    # wait for the login form to load
    try:
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.NAME, "tboxUsuario"))
        )
    except TimeoutError:
        browser.quit()
        return ExitCode.LOGOUT_TIMEOUT

    # Close the browser
    browser.quit()

    return ExitCode.SUCCESS

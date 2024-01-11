# -*- coding: utf-8 -*-

"""
# Language: Python 3
# Written by: Manuel Martinez
# Description: Selenium script for marking the hours in the workday.
"""

from datetime import datetime
from time import sleep

from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from work_time_logger import config
from work_time_logger.hour_marker import ExitCode



def press_cheker_button():
    """Press the button for marking the entrance/exit hour."""

    # Create the options for the browser
    options = ChromeOptions()
    options.add_argument("--headless")

    # Get sensitive data from the config file
    username = config.USERNAME
    password = config.PASSWORD
    website = config.LOGGING_WEBSITE

    # Declare xpaths as constants
    USERNAME_XPATH = '//*[@id="tuEmail"]'
    PASSWORD_XPATH = '//*[@id="tuPassword"]'
    LOGIN_BUTTON_XPATH = '//*[@id="intro"]/div/form/span/button'
    TRIGGER_BUTTON_XPATH = '//*[@id="root"]/div[2]/main/div[1]/div[1]/div/div/div/div[3]/div/div[2]/button'
    TIMER_XPATH = '//*[@id="root"]/div[2]/main/div[1]/div[1]/div/div/div/div[3]/div/div[1]/p'

    # Create the browser
    browser = webdriver.Chrome(options=options)

    # Go to the web page
    browser.get(website)

    # wait for login form to load
    try:
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "tuEmail"))
        )
    except TimeoutError:
        browser.quit()
        return ExitCode.LOGIN_TIMEOUT

    # Fill the login form
    browser.find_element(By.XPATH, USERNAME_XPATH).send_keys(username)
    browser.find_element(By.XPATH, PASSWORD_XPATH).send_keys(password)
    browser.find_element(By.XPATH , LOGIN_BUTTON_XPATH).click()

    # wait for the main page to load
    try:
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    TRIGGER_BUTTON_XPATH
                )
            )
        )
    except TimeoutError:
        browser.quit()
        return ExitCode.LOGIN_TIMEOUT

    # Check if the button was already pressed
    trigger_button = browser.find_element(
        By.XPATH,
        TRIGGER_BUTTON_XPATH
    )

    button_text = trigger_button.text
    timer_text = browser.find_element(By.XPATH, TIMER_XPATH).text
    time_atm = datetime.now()

    if time_atm.hour > 12:
        if timer_text == "00:00:00" or button_text == "Entrar":
            browser.quit()
            return ExitCode.ALREADY_MARKED
    elif time_atm.hour < 12:
        if timer_text != "00:00:00" or button_text == "Salir":
            browser.quit()
            return ExitCode.ALREADY_MARKED

    # Click the button for marking the entrance hour
    trigger_button.click()

    while button_text == trigger_button.text:
        sleep(1)

    # Close the browser
    browser.quit()

    return ExitCode.SUCCESS

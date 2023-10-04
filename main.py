# -*- coding: utf-8 -*-

"""
# Language: Python 3
# Written by: Manuel Martinez
# Description: Core module for the work_time_logger package.
"""


from datetime import datetime, timedelta
from log_manager.logs import LogManager
from work_time_logger.hour_marker import ExitCode, mark_working_hours
from work_time_logger.workday_checker import is_date_workday


logger = LogManager().get_logger()


def main():
    """Main function for the work_time_logger package."""
    # Get yesterday's date
    date = datetime.now() - timedelta(days=1)

    # Check if the date is a workday
    if not is_date_workday(date):
        logger.info("%s is not a workday.", date.strftime('%Y-%m-%d'))
        return

    # Mark the working hours
    exit_code = mark_working_hours(date)

    # log result
    if exit_code == ExitCode.SUCCESS:
        logger.info("Hours marked successfully.")
    elif exit_code == ExitCode.LOGIN_TIMEOUT:
        logger.error("Login timeout.")
    elif exit_code == ExitCode.IN_DATE_ERROR:
        logger.error("Error setting the in date.")
    elif exit_code == ExitCode.OUT_DATE_ERROR:
        logger.error("Error setting the out date.")
    elif exit_code == ExitCode.LOGOUT_TIMEOUT:
        logger.error("Logout timeout.")
    else:
        logger.error("Unknown error.")

    return


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-

"""
# Language: Python 3
# Written by: Manuel Martinez
# Description: Manage log configuration for the application
"""

import os

from datetime import datetime
from logging import FileHandler, Formatter, getLogger, INFO


class LogManager:
    """Manage log configuration for the application"""

    def __init__(self, log_level=INFO):
        """Initialize the LogManager class"""
        today_date = datetime.now().strftime('%Y-%m')

        logs_script_path = os.path.realpath(__file__)
        logs_script_directory = os.path.dirname(logs_script_path)
        logs_base_path = os.path.join(logs_script_directory, '..', 'logs')
        logs_base_path = os.path.normpath(logs_base_path)

        log_file_name = f'{today_date}.log'

        self.log_file = os.path.join(logs_base_path, log_file_name)

        self.logger = getLogger()

        self.set_log_level(log_level)
        self.log_level = log_level

        self.formatter = Formatter(
            '%(asctime)s - %(levelname)s - %(message)s')

        self.set_log_file()

    def set_log_file(self):
        """Set the log file for the application"""
        file_handler = FileHandler(self.log_file)
        file_handler.setLevel(self.log_level)
        file_handler.setFormatter(self.formatter)
        self.logger.addHandler(file_handler)

    def set_log_level(self, log_level):
        """Set the log level for the application"""
        self.logger.setLevel(log_level)

    def get_logger(self):
        """Return the logger"""
        return self.logger

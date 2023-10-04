==================================
Working Hours Logger Documentation
==================================

This project is designed to automate the process of logging working hours. 

It is designed to work with my company's specific website for logging hours.

The script is designed to be run on a daily basis, and it will automatically log the hours for the previous day.

It logs the previous day due to the following limitations and rules:

1. The website does not allow logging future hours.

2. The website allows logging hours for the current and previous day.

TODO list
=========

1. **Modular Hour Marking**: Make the script to mark the hours in a more modular way.

2. **Hour Randomizer**: Apply a randomizer to the working hours to make the logged hours seem more natural.

3. **Web Scraper for Non-Working Days in the current year**: Automatically obtain non-working days using a web scraper for an Specified Area.

4. **Vacation Days Input**: Provide an easy way to input vacation days into the system. Maybe a GUI to configure everything.

5. **Make a better logging System**: Make a better logging system that is more modular and easier to use.

6. **Automatically set up jobs**: Automate the process of setting up the daily job in the system.

**Note**: I will be adding more items to this list as I think of them.

Installation
============

To install this project, you can clone the repository using the following command:

.. code-block:: bash

    git clone https://https://github.com/thriskel/work_time_logger.git

Then, navigate into the project directory and install the required dependencies:

.. code-block:: bash

    cd work_time_logger
    pip install -r requirements.txt

Configuration
=============

To configure this project, you will need to create a ``config.py`` file in the work_time_logger directory in the project.

In this file, you will need to add the following variables:

.. code-block:: python

    LOGGING_WEBSITE = "website_login_url"
    USERNAME = "username"
    PASSWORD = "password"
    START_HOUR = 8 # integer value (24 hour format), this is the hour that you start working
    START_MINUTE = 0 # integer value (24 hour format), this is the minute that you start working
    END_HOUR = 16 # integer value (24 hour format), this is the hour that you end working
    END_MINUTE = 30 # integer value (24 hour format), this is the minute that you end working
    FRIDAY_END_HOUR = 15 # integer value (24 hour format), this is the hour that you end working on fridays
    FRIDAY_END_MINUTE = 0 # integer value (24 hour format), this is the minute that you end working on fridays
    PLACE_VALUE = "selector_option_name" # this is the value of the place where you work

Usage
=====

To use this project, you can run the main script using the following command:

.. code-block:: bash

    python main.py

If you wish to run the script on a daily basis as for now you will need to set up a cron job, or a scheduled task.

Contributing
============

Contributions are welcome! Please read the contributing guidelines before making any changes.

License
=======

This project is licensed under the terms of the MIT license.

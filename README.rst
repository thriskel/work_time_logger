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

    git clone https://github.com/yourusername/working-hours-logger.git

Then, navigate into the project directory and install the required dependencies:

.. code-block:: bash

    cd working-hours-logger
    pip install -r requirements.txt

Usage
=====

To use this project, you can run the main script using the following command:

.. code-block:: bash

    python main.py

Contributing
============

Contributions are welcome! Please read the contributing guidelines before making any changes.

License
=======

This project is licensed under the terms of the MIT license.

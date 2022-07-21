import inspect
import logging

import pytest
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures('setup')
class BaseClass:

    def get_logger(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        filehandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter('%(asctime)s :%(levelname)s : %(name)s :%(message)s')
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)
        return logger

    def select_by_visible_text(self, locator, text):
        Select(locator).select_by_visible_text(text)

    def select_by_index(self, locator, index):
        Select(locator).select_by_index(index)

    def select_by_value(self, locator, value):
        Select(locator).select_by_value(value)


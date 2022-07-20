import pytest
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures('setup')
class BaseClass:

    def select_by_visible_text(self, locator, text):
        Select(locator).select_by_visible_text(text)

    def select_by_index(self, locator, index):
        Select(locator).select_by_index(index)

    def select_by_value(self, locator, value):
        Select(locator).select_by_value(value)


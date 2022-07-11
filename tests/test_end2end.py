import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures('setup')
class TestOne:

    def test_end2end(self, setup):

        username = self.driver.find_element(By.NAME, 'username')
        username.send_keys('john')

        password = self.driver.find_element(By.NAME, 'password')
        password.send_keys('demo')

        submit_button = self.driver.find_element(By.XPATH, '//input[@type="submit"]')
        submit_button.click()

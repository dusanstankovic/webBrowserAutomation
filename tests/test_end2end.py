from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_end2end(self):

        username = self.driver.find_element(By.NAME, 'username')
        username.send_keys('john')

        password = self.driver.find_element(By.NAME, 'password')
        password.send_keys('demo')

        submit_button = self.driver.find_element(By.XPATH, '//input[@type="submit"]')
        submit_button.click()

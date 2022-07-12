from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_end2end(self):

        login_page = LoginPage(self.driver)
        login_page.username_entry().send_keys('john')
        login_page.password_entry().send_keys('demo')
        login_page.submit_button().click()

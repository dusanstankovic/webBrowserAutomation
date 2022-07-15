import time

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from pageObjects.AccountsOverviewPage import AccountsOverviewPage
from pageObjects.LoginPage import LoginPage
from pageObjects.OpenNewAccountPage import OpenNewAccountPage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_end2end(self):

        # Login Page
        login_page = LoginPage(self.driver)
        login_page.username_entry().send_keys('john')
        login_page.password_entry().send_keys('demo')
        login_page.submit_button().click()

        # Accounts Overview Page
        accounts_overview_page = AccountsOverviewPage(self.driver)
        headers = accounts_overview_page.get_headers()
        i = -1
        for header in headers:
            i += 1
            if i == 0:
                assert header.text == 'Account'
            elif i == 1:
                assert header.text == 'Balance*'
            elif i == 2:
                assert header.text == 'Available Amount'
        accounts_overview_page.open_new_account_link().click()

        # Open New Accounts Page
        new_account_page = OpenNewAccountPage(self.driver)

        # Select New Account Type
        selection_new = Select(new_account_page.select_account_type())
        selection_new.select_by_visible_text('SAVINGS')

        # Deposit to current account, select account with index 1 (second on the list)
        selection_current = Select(new_account_page.select_current_account())
        selection_current.select_by_index(0)

        # Submit new account form
        time.sleep(1)
        new_account_page.submit().click()
        time.sleep(1)

        # Confirmation message
        conf_message = new_account_page.confirmation().text
        assert conf_message == 'Account Opened!'

        # Fetch new account number
        new_account_number = new_account_page.get_new_account_number().text


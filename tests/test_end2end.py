import time

from selenium.webdriver.support.select import Select

from pageObjects.LoginPage import LoginPage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_end2end(self):

        # Login Page
        login_page = LoginPage(self.driver)
        login_page.username_entry().send_keys('john')
        login_page.password_entry().send_keys('demo')

        # Accounts Overview Page
        accounts_overview_page = login_page.submit_button()  # clicks the button and returns AccountsOverviewPage object
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

        # Open New Accounts Page
        new_account_page = accounts_overview_page.open_new_account_link()

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

        # Go to Transfer Funds page
        time.sleep(1)
        transfer_funds_page = new_account_page.transfer_funds()
        time.sleep(1)
        # Transfer funds ($50)
        transfer_funds_page.input_transfer_amount().send_keys(50)
        selection_from = Select(transfer_funds_page.select_from_account())

        # Transfer funds from newly created account
        selection_from.select_by_value(new_account_number)
        time.sleep(1)
        transfer_funds_page.transfer_submit().click()
        time.sleep(1)

        # Transfer confirmation message
        time.sleep(30)
        assert transfer_funds_page.transfer_confirmation_message().text == 'Transfer Complete!'

        # Logout
        transfer_funds_page.logout().click()

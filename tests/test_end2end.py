import time

from pageObjects.LoginPage import LoginPage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_end2end(self):

        # Get logger
        log = self.get_logger()

        # Login Page
        login_page = LoginPage(self.driver)
        log.info("Entering credentials")
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
        self.select_by_visible_text(new_account_page.select_account_type(), 'SAVINGS')

        # Deposit to current account, select account with index 1 (second on the list)
        self.select_by_index(new_account_page.select_current_account(), 0)

        # Submit new account form
        time.sleep(1)
        new_account_page.submit().click()
        time.sleep(1)

        # Confirmation message
        conf_message = new_account_page.confirmation().text
        assert conf_message == 'Account Opened!'

        # Fetch new account number
        new_account_number = new_account_page.get_new_account_number().text
        log.info(f"New account created: {new_account_number}")

        # Go to Transfer Funds page
        time.sleep(1)
        transfer_funds_page = new_account_page.transfer_funds()
        time.sleep(1)
        # Transfer funds ($50)
        log.info("Transferring $50 from new account")
        transfer_funds_page.input_transfer_amount().send_keys(50)

        # Transfer funds from newly created account
        self.select_by_value(transfer_funds_page.select_from_account(), new_account_number)
        time.sleep(1)
        transfer_funds_page.transfer_submit().click()
        time.sleep(1)

        # Transfer confirmation message
        time.sleep(5)
        log.info("Checking for successful transfer")
        assert transfer_funds_page.transfer_confirmation_message().text == 'Transfer Complete!'

        # Logout
        log.info("Logging out")
        transfer_funds_page.logout().click()

from pageObjects.AccountsOverviewPage import AccountsOverviewPage
from pageObjects.LoginPage import LoginPage
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


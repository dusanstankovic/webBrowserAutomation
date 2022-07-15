from selenium.webdriver.common.by import By


class AccountsOverviewPage:

    def __init__(self, driver):
        self.driver = driver

    headers = (By.CSS_SELECTOR, '#accountTable th')
    new_account_link = (By.LINK_TEXT, 'Open New Account')

    def get_headers(self):
        return self.driver.find_elements(*AccountsOverviewPage.headers)

    def open_new_account_link(self):
        return self.driver.find_element(*AccountsOverviewPage.new_account_link)

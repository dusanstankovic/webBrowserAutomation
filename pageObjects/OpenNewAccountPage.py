from selenium.webdriver.common.by import By

from pageObjects.TransferFundsPage import TransferFundsPage


class OpenNewAccountPage:

    def __init__(self, driver):
        self.driver = driver

    new_account_selection = (By.ID, 'type')
    current_account_selection = (By.ID, 'fromAccountId')
    submit_button = (By.XPATH, '//input[@value="Open New Account"]')
    confirmation_title = (By.CSS_SELECTOR, '.title')
    new_account_number = (By.XPATH, '//a[@id="newAccountId"]')
    transfer_funds_link = (By.PARTIAL_LINK_TEXT, 'Transfer')

    def select_account_type(self):
        return self.driver.find_element(*OpenNewAccountPage.new_account_selection)

    def select_current_account(self):
        return self.driver.find_element(*OpenNewAccountPage.current_account_selection)

    def submit(self):
        return self.driver.find_element(*OpenNewAccountPage.submit_button)

    def confirmation(self):
        return self.driver.find_element(*OpenNewAccountPage.confirmation_title)

    def get_new_account_number(self):
        return self.driver.find_element(*OpenNewAccountPage.new_account_number)

    def transfer_funds(self):
        self.driver.find_element(*OpenNewAccountPage.transfer_funds_link).click()
        return TransferFundsPage(self.driver)

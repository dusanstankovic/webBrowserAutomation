from selenium.webdriver.common.by import By


class TransferFundsPage:

    def __init__(self, driver):
        self.driver = driver

    transfer_amount = (By.XPATH, '//input[@id="amount"]')
    transfer_from_account = (By.ID, 'fromAccountId')
    transfer_submit_button = (By.CLASS_NAME, 'button')
    transfer_confirmation = (By.XPATH, '//h1[@class="title"]')
    logout_link = (By.LINK_TEXT, 'Log Out')

    def input_transfer_amount(self):
        return self.driver.find_element(*TransferFundsPage.transfer_amount)

    def select_from_account(self):
        return self.driver.find_element(*TransferFundsPage.transfer_from_account)

    def transfer_submit(self):
        return self.driver.find_element(*TransferFundsPage.transfer_submit_button)

    def transfer_confirmation_message(self):
        return self.driver.find_element(*TransferFundsPage.transfer_confirmation)

    def logout(self):
        return self.driver.find_element(*TransferFundsPage.logout_link)

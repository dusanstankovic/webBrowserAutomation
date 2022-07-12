from selenium.webdriver.common.by import By


class AccountsOverviewPage:

    def __init__(self, driver):
        self.driver = driver

    headers = (By.CSS_SELECTOR, '#accountTable th')

    def get_headers(self):
        return self.driver.find_elements(*AccountsOverviewPage.headers)

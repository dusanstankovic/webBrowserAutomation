from selenium.webdriver.common.by import By

from pageObjects.AccountsOverviewPage import AccountsOverviewPage


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    username = (By.NAME, 'username')
    password = (By.NAME, 'password')
    submit = (By.XPATH, '//input[@type="submit"]')

    def username_entry(self):
        return self.driver.find_element(*LoginPage.username)

    def password_entry(self):
        return self.driver.find_element(*LoginPage.password)

    def submit_button(self):
        self.driver.find_element(*LoginPage.submit).click()
        return AccountsOverviewPage(self.driver)

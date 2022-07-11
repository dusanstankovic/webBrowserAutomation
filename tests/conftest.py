import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='class')
def setup(request):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get('https://parabank.parasoft.com/parabank/index.htm?ConnType=JDBC')
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


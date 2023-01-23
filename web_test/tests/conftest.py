import pytest

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service

from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from web_test.helpers.browsers import Browser
from web_test.helpers.project_helpers import get_browser_name
from web_test.helpers.user import User
from web_test.pages.login_page import LoginPage



@pytest.fixture()
def driver():
    browser_name = get_browser_name()
    if browser_name.lower() == Browser.CHROME:
        #path = r''  # TODO: specify path to chromedriver here
        #driver = Chrome(service=Service(path))
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
    elif browser_name.lower() == Browser.FIREFOX:
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    yield driver
    driver.quit()


@pytest.fixture()
def login_page(driver):
    login_page = LoginPage(driver)
    login_page.navigate()
    return login_page


@pytest.fixture(scope='session')
def valid_user():
    return User('standard_user', 'secret_sauce')


@pytest.fixture(scope='session')
def locked_out_user():
    return User('locked_out_user', 'secret_sauce')

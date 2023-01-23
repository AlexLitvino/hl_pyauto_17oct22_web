"""First iteration of tests"""

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import pytest

# TODO: specify path to chromedriver here
path = r''


@pytest.mark.skip(reason='Not implemented yet')
@pytest.mark.layout
def test_login_page_layout():
    raise NotImplementedError


def test_successful_login():
    """
    1. Navigate to base url
    2. Enter 'standard_user' as username
    3. Enter 'secret_sauce' as password
    4. Click Login button.
    Verify that Inventory page is displayed
    """
    driver = Chrome(service=Service(path))
    driver.maximize_window()
    driver.implicitly_wait(5)

    driver.get('https://www.saucedemo.com/')

    valid_user = 'standard_user'
    valid_password = 'secret_sauce'

    username_input_field = driver.find_element(By.ID, 'user-name')
    password_input_field = driver.find_element(By.ID, 'password')
    login_button = driver.find_element(By.ID, 'login-button')

    username_input_field.send_keys(valid_user)
    password_input_field.send_keys(valid_password)
    login_button.click()

    inventory_container = driver.find_element(By.ID, 'inventory_container')
    assert inventory_container.is_displayed()

    driver.quit()


def test_locked_out_login():
    driver = Chrome(service=Service(path))
    driver.maximize_window()
    driver.implicitly_wait(5)

    driver.get('https://www.saucedemo.com/')

    valid_user = 'locked_out_user'
    valid_password = 'secret_sauce'

    username_input_field = driver.find_element(By.ID, 'user-name')
    password_input_field = driver.find_element(By.ID, 'password')
    login_button = driver.find_element(By.ID, 'login-button')

    username_input_field.send_keys(valid_user)
    password_input_field.send_keys(valid_password)
    login_button.click()

    assert login_button.is_displayed()

    error_message = driver.find_element(By.TAG_NAME, 'h3')
    assert error_message.is_displayed()
    assert error_message.text == 'Epic sadface: Sorry, this user has been locked out.'

    username_error_marker = driver.find_element(By.XPATH, "//input[@id='user-name']/following-sibling::*[local-name()='svg']")
    password_error_marker = driver.find_element(By.XPATH, "//input[@id='password']/following-sibling::*[local-name()='svg']")

    assert username_error_marker.is_displayed()
    assert password_error_marker.is_displayed()

    driver.quit()


@pytest.mark.skip(reason='Not implemented yet')
def test_login_without_username():
    raise NotImplementedError


@pytest.mark.skip(reason='Not implemented yet')
def test_login_without_password():
    raise NotImplementedError

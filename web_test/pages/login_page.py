from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from web_test.helpers.project_helpers import get_base_url
from web_test.pages.base_page import BasePage
from web_test.pages.inventory_page import InventoryPage


class LoginPage(BasePage):

    USERNAME_INPUT_FIELD_LOCATOR = (By.ID, 'user-name')
    PASSWORD_INPUT_FIELD_LOCATOR = (By.ID, 'password')
    LOGIN_BUTTON_LOCATOR = (By.ID, 'login-button')
    ERROR_MESSAGE_LOCATOR = (By.TAG_NAME, 'h3')
    USERNAME_ERROR_MARKER_LOCATOR = (By.XPATH, "//input[@id='user-name']/following-sibling::*[local-name()='svg']")
    PASSWORD_ERROR_MARKER_LOCATOR = (By.XPATH, "//input[@id='password']/following-sibling::*[local-name()='svg']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def username_input_field(self):
        return self.element(LoginPage.USERNAME_INPUT_FIELD_LOCATOR)

    @property
    def password_input_field(self):
        return self.element(LoginPage.PASSWORD_INPUT_FIELD_LOCATOR)

    @property
    def login_button(self):
        return self.element(LoginPage.LOGIN_BUTTON_LOCATOR)

    @property
    def error_message(self):
        return self.element(LoginPage.ERROR_MESSAGE_LOCATOR)

    @property
    def username_error_marker(self):
        return self.element(LoginPage.USERNAME_ERROR_MARKER_LOCATOR)

    @property
    def password_error_marker(self):
        return self.element(LoginPage.PASSWORD_ERROR_MARKER_LOCATOR)

    def navigate(self):
        self.driver.get(get_base_url())

    def enter_username(self, username):
        self.username_input_field.send_keys(username)

    def enter_password(self, password):
        self.password_input_field.send_keys(password)

    def click_login_button(self):
        self.login_button.click()

    def _fill_login_form_and_click_login_button(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def perform_successful_login(self, username, password):
        self._fill_login_form_and_click_login_button(username, password)
        inventory_page = InventoryPage(self.driver)
        inventory_page.is_page_displayed()
        return inventory_page

    def perform_unsuccessful_login(self, username, password):
        self._fill_login_form_and_click_login_button(username, password)
        return self

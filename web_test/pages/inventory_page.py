from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from web_test.pages.base_page import BasePage


class InventoryPage(BasePage):

    INVENTORY_CONTAINER_LOCATOR = (By.ID, 'inventory_container')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def inventory_container(self):
        return self.element(InventoryPage.INVENTORY_CONTAINER_LOCATOR)

    def is_page_displayed(self):
        return self.inventory_container.is_displayed()

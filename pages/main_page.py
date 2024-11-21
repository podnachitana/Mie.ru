import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class MainPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    account_btn = "//div[contains(@class, 'btn-icon-face')]"

    # Getters
    def get_account_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.account_btn)))

    # Actions
    def click_account_btn(self):
        self.get_account_btn().click()
        print("Account button was clicked")
        time.sleep(3)

    # Methods
    def authorization(self):
        self.get_current_url()
        self.click_account_btn()


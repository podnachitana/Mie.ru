import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class MyDataPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    my_data_title = "//div[@class='title-zag']"
    logo = "//img[@class='menu__logo-img']"

    # Getters
    def get_my_data_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.my_data_title)))

    def get_logo(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.logo)))

    # Actions

    def click_logo(self):
        self.get_logo().click()
        print("Logo was clicked")
        time.sleep(3)

    # Methods
    def checking(self):
        self.get_current_url()
        self.check_word(self.get_my_data_title(), 'личный кабинет')
        print("Autorization was success")
        self.click_logo()



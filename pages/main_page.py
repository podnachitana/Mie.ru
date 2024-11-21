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
    email = "//input[@id='auth-login_desktop']"
    password = "//input[@id='auth-password_desktop']"
    login_btn = "//*[@id='bl_user_auth']/div/div/div[2]/form/div[5]/input"
    my_data_link = "//*[@id='bl_user_auth']/div/div/div/form/table/tbody/tr[1]/td/div[3]/a"

    # Getters
    def get_account_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.account_btn)))

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_btn)))

    def get_my_data_link(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.my_data_link)))

    # Actions
    def click_account_btn(self):
        self.get_account_btn().click()
        print("Account button was clicked")
        time.sleep(3)

    def input_email(self, email):
        self.get_email().send_keys(email)
        print("Email was added")
        time.sleep(3)

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Password was added")
        time.sleep(3)

    def click_login_btn(self):
        self.get_login_btn().click()
        print("Login button was clicked")
        time.sleep(3)

    def click_my_data_link(self):
        self.get_my_data_link().click()
        print("My data button was clicked")
        time.sleep(3)

    # Methods
    def authorization(self):
        self.get_current_url()
        self.click_account_btn()
        self.input_email("tatianaterrible@yandex.ru")
        self.input_password("bammargera1979")
        self.click_login_btn()

    def my_account(self):
        self.get_current_url()
        self.click_account_btn()
        self.click_my_data_link()

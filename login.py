from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils import Utils


class Login:
    def __init__(self, browser):
        self.browser = browser

    def login(self, username, password):
        try:
            username_input = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            password_input = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.NAME, "password"))
            )

            submit_button = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[@type='submit']"))
            )
            Utils.random_short_sleep()
            username_input.send_keys(username)
            password_input.send_keys(password)
            submit_button.click()
        except:
            print("Error could not login")

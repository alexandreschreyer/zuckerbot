from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import states
from utils import Utils


class Login:
    def __init__(self, browser, gui, botlogic_instance):
        self.browser = browser
        self.gui = gui
        self.botlogic_instance = botlogic_instance
        self._short_wait_time = 3
        self._medium_wait_time = 10

    def login(self, username, password):
        if self.is_user_logged_in():
            self.gui.log("User already logged in")
        else:
            self.gui.log("Trying to log in...")
            try:
                username_input = WebDriverWait(self.browser, self._medium_wait_time).until(
                    EC.presence_of_element_located((By.NAME, "username"))
                )
                password_input = WebDriverWait(self.browser, self._medium_wait_time).until(
                    EC.presence_of_element_located((By.NAME, "password"))
                )

                submit_button = WebDriverWait(self.browser, self._medium_wait_time).until(
                    EC.presence_of_element_located((By.XPATH, "//button[@type='submit']"))
                )
                Utils.random_short_sleep()
                username_input.send_keys(username)
                password_input.send_keys(password)
                submit_button.click()
            except:
                self.gui.log("Error could not login, stopping bot")
                self.botlogic_instance.set_state(states.State.STOPPED)

    def is_user_logged_in(self):
        try:
            with Utils.wait_for_page_load(self.browser, timeout=10):
                self.browser.find_element_by_link_text("Search")
        except NoSuchElementException:
            return False

        return True

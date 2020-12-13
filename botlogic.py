import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from webdriver_manager.chrome import ChromeDriverManager

import states
from login import Login


class BotLogic(threading.Thread):
    _instance = None

    def __init__(self, threadID, name, counter, gui):
        if BotLogic._instance is None:
            self.state = states.State.STOPPED
            threading.Thread.__init__(self)
            self.threadID = threadID
            self.name = name
            self.counter = counter
            self.gui = gui
            BotLogic._instance = self
        else:
            raise Exception("Singleton: You cannot create another Logic class")

    def run(self):
        self.run_bot()

    @staticmethod
    def get_instance(gui):
        if not BotLogic._instance:
            BotLogic(1, "thread_1", 1, gui)
        return BotLogic._instance

    def get_state(self):
        return self.state

    def set_state(self, new_state):
        self.state = new_state

    def run_bot(self):
        while True:
            sleep(1)
            if self.state == states.State.STARTED:
                self.gui.log("Bot started")
                browser = webdriver.Chrome(ChromeDriverManager().install())
                browser.get('https://www.instagram.com/')

                login = Login(browser, self.gui, self)
                login.login("", "")
            if self.state == states.State.STOPPED:
                self.gui.btn_go_text.set("Start")


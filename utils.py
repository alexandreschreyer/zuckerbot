from contextlib import contextmanager
from time import sleep
import random

from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.support.wait import WebDriverWait


class Utils:

    @staticmethod
    def random_short_sleep():
        sleep_time = random.uniform(0.5, 2.5)
        sleep(sleep_time)

    @staticmethod
    @contextmanager
    def wait_for_page_load(browser, timeout=30):
        old_page = browser.find_element_by_tag_name('html')
        yield
        WebDriverWait(browser, timeout).until(
            staleness_of(old_page)
        )
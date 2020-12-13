from time import sleep
import random


class Utils:

    @staticmethod
    def random_short_sleep():
        sleep_time = random.uniform(0.5, 2.5)
        sleep(sleep_time)
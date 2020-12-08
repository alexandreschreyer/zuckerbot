from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://www.instagram.com/')

sleep(5)
login_link = browser.find_element_by_name("username")
login_link.click()

browser.close()
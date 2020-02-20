from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()

browser.get('https://www.facebook.com')
time.sleep(1)
email = browser.find_element_by_id('email')
email.send_keys('9806878493')
password = browser.find_element_by_id('pass')
password.send_keys('iamryan')
email.submit()
time.sleep(3)
browser.get(browser.current_url+'/messages')

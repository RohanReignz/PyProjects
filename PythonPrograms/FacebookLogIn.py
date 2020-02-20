from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get('https://www.facebook.com')
time.sleep(2)
browser.find_element_by_id('email').send_keys('9806878493')
pw = browser.find_element_by_id('pass')
pw.send_keys('iamryan'+Keys.RETURN)

time.sleep(2)


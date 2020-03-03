from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get("https://10fastfingers.com/typing-test/english")
time.sleep(2)
inp = browser.find_element_by_id('inputfield')

while True:
    high = browser.find_element_by_class_name('highlight')
    inp.send_keys(high.text+Keys.SPACE)

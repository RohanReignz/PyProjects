from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
name = str(input("Keyword: "))
choice = int(input("What numbered? "))
browser = webdriver.Chrome()
browser.get("https://www.youtube.com")
browser.find_element_by_id('search').send_keys(name+Keys.RETURN)
time.sleep(1)
links = browser.find_elements_by_id('title-wrapper')
links[choice-1].click()

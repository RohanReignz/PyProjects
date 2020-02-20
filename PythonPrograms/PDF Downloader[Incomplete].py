from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
search = str(input("Enter book name: "))
new =search.replace(" ", "+")
browser = webdriver.Chrome()
browser.get("https://www.pdfdrive.com/search?q="+new)
time.sleep(3)
div = []
div = browser.find_elements_by_class_name('file-right')
for s in div:
	link = s.find_element_by_css_selector('a').get_attribute('href')
	browser.get(link)
	browser.find_element_by_id('download-button-link').click()
	time.sleep(10)
	dive = browser.find_element_by_id('alternatives')
	download=dive.find_element_by_css_selector('a').get_attribute('href')
	browser.get(download)

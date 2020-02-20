from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
name = str(input("Whose? "))
choice = int(input("Ranked what? "))
browser = webdriver.Chrome()
browser.get("https://www.youtube.com")
browser.find_element_by_id('search').send_keys(name+Keys.RETURN)
time.sleep(1)
browser.find_element_by_id('main-link').click()
browser.get(browser.current_url+'/videos?view=0&sort=p')
links = browser.find_elements_by_id('video-title')
links[choice-1].click()

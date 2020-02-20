from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
youtuber = str(input("Enter search word:"))
choice = int(input("Which video do you want to play?"))
browser = webdriver.Chrome()
browser.get('https://www.youtube.com')
time.sleep(1)
search = browser.find_element_by_id('search')
search.send_keys('%s'%(youtuber))
search_key = browser.find_element_by_id('search-icon-legacy')
search_key.click()
time.sleep(1)
links=[]
links = browser.find_elements_by_class_name('style-scope ytd-video-renderer')
links[choice-1].click()

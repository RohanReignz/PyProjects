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
browser.get('https://www.facebook.com/gita.giri.52/photos')
time.sleep(2)
photos=[]
photos = browser.find_elements_by_class_name('tagWrapper')
for i in range(len(photos)):
	photos = browser.find_elements_by_class_name('tagWrapper')
	photos[i].click()
	time.sleep(2)
	browser.find_element_by_class_name('_666k').click()
	time.sleep(1)
	browser.get('https://www.facebook.com/gita.giri.52/photos')
	time.sleep(3)




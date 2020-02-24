import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def autoliker():
	i = 0
	while i!=50:
		i+=1
		pyautogui.click(784, 391)
		time.sleep(1)
		like = pyautogui.locateCenterOnScreen('like.png', confidence=0.6)
		pyautogui.click(like)
		time.sleep(1)


browser = webdriver.Chrome()
browser.get('https://www.facebook.com')
time.sleep(1)
browser.find_element_by_id('email').send_keys('Your_email')
browser.find_element_by_id('pass').send_keys('Your_password'+Keys.RETURN)
time.sleep(1)
person = "Link_to_person's_first_photo_on_profile" #Link to photo
browser.get(person)
time.sleep(3)
autoliker()






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
browser.find_element_by_id('email').send_keys('9806878493')
browser.find_element_by_id('pass').send_keys('iamryan'+Keys.RETURN)
time.sleep(1)
person = "https://www.facebook.com/photo.php?fbid=2544270245804246&set=pob.100006638853129&type=3&theater" #Link to photo
browser.get(person)
time.sleep(3)
autoliker()






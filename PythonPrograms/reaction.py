import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import time

browser = webdriver.Chrome()
browser.get('https://www.humanbenchmark.com/tests/reactiontime')
time.sleep(2)
pos = pyautogui.position()
pyautogui.click(pos)
try:
	element = WebDriverWait(browser, 20).until(EC.presence_of_element_located(By.CLASS_NAME, "test-standard reaction-time-test view-go"))
	pyautogui.click(pos)
finally:
	browser.quit()

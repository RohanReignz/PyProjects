import pyautogui
import time

start = pyautogui.locateCenterOnScreen('the.png')
while start==None:
	start = pyautogui.locateCenterOnScreen('the.png', confidence=0.9)
	if start!=None:
		pyautogui.click()		


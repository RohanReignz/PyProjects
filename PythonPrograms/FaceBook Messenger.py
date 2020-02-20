from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

mes = str(input("What would you like to send? "))
who = str(input("To whom? "))
choice = int(input("Would you like to keep the browser open? "))
who_l = who.lower()
if who_l == "dipin":
	who_l = "https://www.facebook.com/messages/t/dipin.bk.94"
elif who_l == "shashank":
	who_l = "https://www.facebook.com/messages/t/shashank.shadow.whicir"
elif who_l == "razwol":
	who_l = "https://www.facebook.com/messages/t/razzwol.chapagain.1"
elif who_l == "pimps":
	who_l = "https://www.facebook.com/messages/t/4213437788681959"
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
browser = webdriver.Chrome(options=chrome_options)
browser.get('https://www.facebook.com')
time.sleep(1)
email = browser.find_element_by_id('email')
email.send_keys('9806878493')
password = browser.find_element_by_id('pass')
password.send_keys('iamryan')
email.submit()
time.sleep(2)
browser.get(who_l)
time.sleep(3)
y = browser.find_element_by_xpath('//div[contains(@aria-label, "Type a message")]')
y.send_keys(mes+Keys.RETURN)
time.sleep(2)
if choice != 1:
	browser.close()

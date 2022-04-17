import pyautogui, sys
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

	#Opens passed link and closes browser after opening
def open_meeting(link):
	driver = webdriver.Chrome()
	driver.get(link)
	time.sleep(3)
	pyautogui.click(x=777, y=300, clicks=1, interval=0, button='left')
	driver.close()

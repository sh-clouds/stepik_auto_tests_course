from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time 
import math
import os


def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))


try:
	browser = webdriver.Chrome()
	browser.get("http://suninjuly.github.io/explicit_wait2.html")

	# говорим WebDriver ждать все элементы в течение 5 секунд
	# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
	WebDriverWait(browser, 12).until(
	        EC.text_to_be_present_in_element((By.ID, "price"),'100')
	    )
	button = browser.find_element(By.ID, "book")
	button.click()


	x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
	x = x_element.text
	y = calc(x)
	#print (y)
	input1 = browser.find_element(By.ID,"answer")
	input1.send_keys(y)

	button = browser.find_element(By.ID, "solve")
	#browser.execute_script("return arguments[0].scrollIntoView(true);", button)
	button.click()	


finally:
	time.sleep(60)
	browser.quit()
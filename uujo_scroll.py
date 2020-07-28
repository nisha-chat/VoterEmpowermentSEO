from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import random
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait

def scrollWebsite(driver):
	times = [5,6,7,8,9,10,11,12,13,14,15, 16, 17, 18, 19, 20, 21, 22, 23, 24]


	time.sleep(random.choice(times))
	driver.find_element_by_xpath("//span[contains(text(),'Programs')]").click()
	print(driver.current_url)

	time.sleep(random.choice(times))
	driver.find_element_by_xpath("//span[contains(text(),'Anti-Racism')]").click()
	print(driver.current_url)

	time.sleep(random.choice(times))
	driver.find_element_by_xpath("//span[contains(text(),'Take Action')]").click()
	print(driver.current_url)

	time.sleep(random.choice(times))
	driver.find_element_by_xpath("//span[contains(text(),'About Us')]").click()
	print(driver.current_url)

	time.sleep(random.choice(times))
	driver.find_element_by_xpath("//span[contains(text(),'Contact Us')]").click()
	print(driver.current_url)

	time.sleep(random.choice(times))
	driver.find_element_by_xpath("//span[contains(text(),'Join Us')]").click()
	print(driver.current_url)
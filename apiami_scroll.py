from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import random
import time

def scrollWebsite(driver):
	times = [5,6,7,8,9,10,11,12,13,14,15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
	time.sleep(20)
	driver.find_element_by_link_text("ABOUT").click()
	print(driver.current_url)
	time.sleep(random.choice(times))
	driver.find_element_by_link_text("OUR WORK").click()
	print(driver.current_url)
	time.sleep(random.choice(times))
	driver.find_element_by_link_text("GET INVOLVED").click()
	print(driver.current_url)
	time.sleep(random.choice(times))
	driver.find_element_by_link_text("DONATE").click()
	print(driver.current_url)
	time.sleep(random.choice(times))
	driver.find_element_by_link_text("CONTACT").click()
	print(driver.current_url)
	time.sleep(random.choice(times))


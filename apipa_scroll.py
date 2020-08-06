from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import random
import time

def scrollWebsite(driver):
	times = [5,6,7,8,9,10,11,12,13,14,15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

	driver.find_element_by_xpath("//a[text()='ABOUT']").click()
	print(driver.current_url)
	time.sleep(random.choice(times))
	driver.find_element_by_xpath("//a[text()='ADVOCACY']").click()
	print(driver.current_url)
	time.sleep(random.choice(times))
	driver.find_element_by_xpath("//a[text()='EVENTS']").click()
	print(driver.current_url)
	time.sleep(random.choice(times))
	driver.find_element_by_xpath("//a[text()='PRESS']").click()
	print(driver.current_url)
	time.sleep(random.choice(times))
	driver.find_element_by_xpath("//a[text()='CONTACT']").click()
	print(driver.current_url)
	time.sleep(random.choice(times))
	print(driver.current_url)
	driver.find_element_by_xpath("//span[contains(text(),'DONATE')]").click()
	print(driver.current_url)
	time.sleep(random.choice(times))
	print(driver.current_url)


from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import random
import time

def scrollWebsite(driver):
	times = [5,6,7,8,9,10,11,12,13,14,15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
	driver.find_element_by_xpath("//a[text()='About']").click()
	print(driver.current_url)
	time.sleep(random.choice(times))
	driver.find_element_by_xpath("//a[text()='Volunteer']").click()
	print(driver.current_url)
	time.sleep(random.choice(times))
	driver.find_element_by_xpath("//a[text()='Partners']").click()
	print(driver.current_url)
	time.sleep(random.choice(times))
	driver.find_element_by_xpath("//a[text()='Donate']").click()
	print(driver.current_url)
	time.sleep(random.choice(times))
	driver.find_element_by_xpath("//a[text()='Contact']").click()
	print(driver.current_url)
	time.sleep(random.choice(times))
	print(driver.current_url)


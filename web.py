from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import random
import time
def scrollWebsite():
	times = [5,6,7,8,9,10,11,12,13,14,15]

	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument('--no-sandbox')
	chrome_options.add_argument('--window-size=1420,1080')
	chrome_options.add_argument('--headless')
	chrome_options.add_argument('--disable-gpu')
	driver = webdriver.Chrome(chrome_options=chrome_options)

	driver.get('https://empowervoters.us/')
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


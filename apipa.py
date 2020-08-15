from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from apipa_scroll import scrollWebsite
import random
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1420,1080')
chrome_options.add_argument('--headless')
chrome_options.add_argument("--incognito")
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage') 

sessions = 1

while True:
	driver = webdriver.Chrome(options=chrome_options)
	count = 0
	driver.get('http://www.google.com')
	driver.implicitly_wait(10)
	search_field = driver.find_element_by_name("q")
	search_field.send_keys("Asian Pacific Islander Vote Pennsylvania")
	search_field.submit()

	driver.implicitly_wait(15)
	driver.find_element_by_xpath('//a[starts-with(@href,"https://www.facebook.com/apipennsylvania/?ref=py_c")]').click()
	driver.implicitly_wait(5)

	page = count + 1
	print("#" + str(sessions) + ": 'Asian Pacific Islander Vote Pennsylvania' - Page ", page)

	#driver.find_element_by_xpath('//a[starts-with(@href,"http://apipennsylvania.org/")]').click()
	driver.find_element_by_link_text('apipennsylvania.org').click()
	driver.implicitly_wait(15)
	driver.switch_to.window(driver.window_handles[1])
	driver.implicitly_wait(5)
	print(driver.current_url)
	sessions += 1
	time.sleep(20)
	scrollWebsite(driver)

	driver.quit()


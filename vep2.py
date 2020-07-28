from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from vep_scroll import scrollWebsite
import random
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1420,1080')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)

sessions = 1

while True:
	loop = True
	count = 0
	driver.get('http://www.google.com')
	driver.implicitly_wait(10)
	search_field = driver.find_element_by_name("q")
	search_field.send_keys("voter empowerment")
	search_field.submit()
	driver.implicitly_wait(3)
	print("URL: " + driver.current_url)
	while loop:
		try:
			driver.find_element_by_xpath('//a[starts-with(@href,"https://empowervoters.us/")]').click()
			page = count + 1
			print("#" + str(sessions) + ": 'voter empowerment - Page ", page)
			scrollWebsite(driver)
			sessions += 1
			time.sleep(5)
			loop = False
		except NoSuchElementException:
		    driver.execute_script("window.scrollTo(0, 5000)")
		    driver.find_element_by_link_text("Next").click()
		    time.sleep(2)
		    count +=1

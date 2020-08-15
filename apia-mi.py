from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from apiami_scroll import scrollWebsite
import random
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1420,1080')
chrome_options.add_argument('--headless')
chrome_options.add_argument("--incognito")
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage') 
driver = webdriver.Chrome(options=chrome_options)

sessions = 1

while True:
	loop = True
	count = 0
	driver.get('http://www.google.com')
	driver.implicitly_wait(10)
	search_field = driver.find_element_by_name("q")
	search_field.send_keys("Voter Empowerment Michigan")
	#Asian Americans Vote Michigan
	search_field.submit()
	driver.implicitly_wait(3)
	while loop:
		print("Page: " + str(count+1))
		try:
			driver.implicitly_wait(15)
			#driver.find_element_by_xpath('//a[starts-with(@href,"https://www.apiavotemi.org/")]').click()
			driver.find_element_by_xpath('//a[starts-with(@href,"https://www.apiavote.org/partner-organizations")]').click()
			driver.implicitly_wait(5)
			driver.find_element_by_link_text("APIAVote - Michigan").click()
			page = count + 1
			print("#" + str(sessions) + ": 'Voter Empowerment Michigan' - Page ", page)

			driver.implicitly_wait(15)
			print(driver.current_url)
			scrollWebsite(driver)
			sessions += 1
			time.sleep(20)
			loop = False
		except NoSuchElementException:
		    driver.execute_script("window.scrollTo(0, 5000)")
		    driver.find_element_by_link_text("Next").click()
		    time.sleep(5)
		    count +=1

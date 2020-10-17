from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from uujo_scroll import scrollWebsite
import random
import time

sessions = 0

while True:
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument('--no-sandbox')
	chrome_options.add_argument('--window-size=1420,1080')
	chrome_options.add_argument('--headless')
	chrome_options.add_argument("--incognito")
	chrome_options.add_argument('--disable-gpu')
	chrome_options.add_argument('--disable-dev-shm-usage')
	path = "/Users/nchatwani/Desktop/chromedriver"
	driver = webdriver.Chrome(path, options=chrome_options)
	#loop = True
	#count = 0
	driver.get('http://www.google.com')
	driver.implicitly_wait(10)
	search_field = driver.find_element_by_name("q")
	search_field.send_keys("Voter Enrichment Pittsburgh")
	search_field.submit()
	driver.implicitly_wait(15)
	#print("Page: " + str(count+1))
	#try:
	#driver.find_element_by_xpath('//a[starts-with(@href,"http://veeempittsburgh.org/")]').click()
	driver.find_element_by_xpath('//a[starts-with(@href, "https://www.facebook.com/VEEEMPittsburgh/")]').click()
	#driver.find_element_by_link_text("").click()
	driver.implicitly_wait(5)
	driver.find_element_by_link_text("www.veeempittsburgh.org").click()
	#page = count + 1
	#print("#" + str(sessions) + ": 'Pittsburgh Voting' - Page ", page)
	time.sleep(60)
	sessions += 1
	print(sessions)
	driver.quit()
	# except NoSuchElementException:
	#     driver.execute_script("window.scrollTo(0, 5000)")
	#     driver.find_element_by_link_text("Next").click()
	#     time.sleep(5)
	    #count +=1




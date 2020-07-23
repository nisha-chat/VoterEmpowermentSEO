#!/usr/bin/env python3
#enter command into terminal
#cd ~/Desktop
#python3 staffing.py

import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-infobars")
#chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

driver.get('https://www.sourcing.games/game-6/game-6-c7abh/')
time.sleep(120)
for x in range (1800,1999):
    driver.execute_script("window.scrollTo(0,500)")
    el = driver.find_element_by_id("pwbox-833274435")
    el.send_keys(x)
    print(x)
    el.send_keys(Keys.ENTER)
    time.sleep(5)

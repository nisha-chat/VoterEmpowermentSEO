from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1420,1080')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://empowervoters.us/')
el = driver.find_element_by_class_name('toggle nav-toggle desktop-nav-toggle')
print(el.text)

el.click()
print(driver.current_url)
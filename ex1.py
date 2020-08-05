from selenium import webdriver
import os,time

driver = webdriver.Chrome(f"{os.getcwd()}/chromedriver")

driver.get('https://jasim.tech/automation/one/')
time.sleep(2)

search_input = driver.find_element_by_name('name')
search_input.send_keys('Python Programming Language')

time.sleep(2)

search_btn = driver.find_element_by_css_selector("input[type='submit']")
search_btn.click()

time.sleep(2)

# driver.close()
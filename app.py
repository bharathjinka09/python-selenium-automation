from selenium import webdriver
import os
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome(f"{os.getcwd()}/chromedriver")
driver.get('https://www.google.com')
driver.close()
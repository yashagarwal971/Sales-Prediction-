import time

from selenium import webdriver
import csv
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome("C:\\Users\\anees\\Downloads\\chromedriver.exe")  # Optional argument, if not specified will search path.

driver.get("D:/Projects/Tourism-data-analysis/index.html")

# Maximize the window and let code stall 
# for 8s to properly maximise the window.
driver.maximize_window()
time.sleep(8)
  
# Obtain button by link text and click.
button = driver.find_element_by_link_text("inbound tourism analysis")
button.click()

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 



button2 = driver.find_element_by_link_text("outbound tourists analysis")
button2.click()

button3 = driver.find_element_by_link_text("GDP and tourism")
button3.click()

button4 = driver.find_element_by_link_text("Summary")
button4.click()

button5 = driver.find_element_by_link_text("Home page")
button5.click()

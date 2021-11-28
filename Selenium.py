import time

from selenium import webdriver
import csv
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome("C:\\Users\\anees\\Downloads\\chromedriver.exe")  # Optional argument, if not specified will search path.

driver.get("file:///D:/Projects/Tourism-data-analysis/index.html")

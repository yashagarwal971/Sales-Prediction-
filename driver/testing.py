from selenium import webdriver
import time
  
driver = webdriver.Firefox(r"/home/samarthgangwal/sales_prediction/driver")
  
driver.get("http://127.0.0.1:5500/index.html")
  
# Maximize the window and let code stall 
# for 8s to properly maximise the window.
driver.maximize_window()
time.sleep(8)

# Obtain button by link text and click.
height = driver.execute_script("return document.body.scrollHeight")
for scrol in range(150,height,150):
    driver.execute_script(f"window.scrollTo(0,{scrol})")
    time.sleep(1.5)

button = driver.find_element_by_link_text("inbound tourism analysis")
button.click()

height = driver.execute_script("return document.body.scrollHeight")
for scrol in range(150,height,150):
    driver.execute_script(f"window.scrollTo(0,{scrol})")
    time.sleep(1.5)

button2 = driver.find_element_by_link_text("outbound tourists analysis")
button2.click()

height = driver.execute_script("return document.body.scrollHeight")
for scrol in range(150,height,150):
    driver.execute_script(f"window.scrollTo(0,{scrol})")
    time.sleep(1.5)

button2 = driver.find_element_by_link_text("GDP and tourism")
button2.click()

height = driver.execute_script("return document.body.scrollHeight")
for scrol in range(150,height,150):
    driver.execute_script(f"window.scrollTo(0,{scrol})")
    time.sleep(1.5)

button4 = driver.find_element_by_link_text("Summary")
button4.click()

height = driver.execute_script("return document.body.scrollHeight")
for scrol in range(150,height,150):
    driver.execute_script(f"window.scrollTo(0,{scrol})")
    time.sleep(1.5)

button5 = driver.find_element_by_link_text("Predictions")
button5.click()

height = driver.execute_script("return document.body.scrollHeight")
for scrol in range(150,height,150):
    driver.execute_script(f"window.scrollTo(0,{scrol})")
    time.sleep(1.5)
# https://www.seleniumeasy.com/test/basic-first-form-demo.html
# Add case for Two Input Fields block

from selenium import webdriver
from selenium.webdriver.common.by import By

import time

TEST_DATA = {
        'single_input': 'My best message here!!',
        'two_input_first': 333,
        'two_input_second': 444
    }

driver = webdriver.Chrome()

driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")
time.sleep(5)
if driver.find_element_by_id("at-cv-lightbox-close").size != 0:
   driver.find_element_by_id("at-cv-lightbox-close").click()


driver.find_element(By.CSS_SELECTOR, "input#user-message").send_keys(TEST_DATA['single_input'])
driver.find_element(By.CSS_SELECTOR, "form#get-input button").click()

assert driver.find_element(By.ID, "display").text == TEST_DATA['single_input']

driver.find_element(By.CSS_SELECTOR, "#sum1").send_keys(TEST_DATA['two_input_first'])
driver.find_element(By.CSS_SELECTOR, "#sum2").send_keys(TEST_DATA['two_input_second'])
driver.find_element(By.CSS_SELECTOR, "#gettotal > button").click()

assert driver.find_element(By.CSS_SELECTOR, "#displayvalue").text == str(TEST_DATA['two_input_first'] + TEST_DATA['two_input_second'])

driver.quit()



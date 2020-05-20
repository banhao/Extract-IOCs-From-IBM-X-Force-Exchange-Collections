# Extract_IOCs_From_IBM_XForce_Exchange_Collections.py
#_*_coding: utf-8_*_

import sys, unittest, time, datetime
import urllib.request, urllib.error, urllib.parse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import InvalidArgumentException

url = sys.argv[1]
#driver=webdriver.Firefox()
driver=webdriver.Chrome()
driver.maximize_window()
driver.get(url)
time.sleep(2)
driver.find_element(By.ID, "termsCheckbox").click()
driver.find_element(By.LINK_TEXT, "... or enter as a Guest").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".show-more-btn").click()
time.sleep(2)

iocTableTitle = driver.find_elements_by_css_selector("#iocTableTitle")
IOCnumber = int(iocTableTitle[0].text.split('(')[-1].split(')')[0])
count = 0

while True:
	element = driver.find_elements_by_css_selector("[ng-if^='row.entity.type !==']")
	for ioc in element:
		iochref = ioc.text
		print(iochref)
		f = open('IBM_X_Force_Collections.list','a+')
		f.write(iochref + "\n")
		count += 1
	driver.execute_script("arguments[0].scrollIntoView(true);", ioc)
	time.sleep(0.5)
	if count > IOCnumber:
		break
f.close

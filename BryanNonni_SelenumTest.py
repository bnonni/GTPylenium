#!/usr/bin/env python3
# coding: utf-8
import os
import re
from sys import exit
import time as t
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

#Declare all variables
browser = ''
operating_system = ''
version = ''
website = 'https://oscar.gatech.edu/'
schedule = "//*[contains(text(), 'Schedule of ')]"
spring = "//*[contains(text(), 'Spring 2019')]"
select = "//input[@value='Submit']"
cs = "//*[contains(text(), 'Computer Science')]"
# acct = "//*[contains(text(), 'Accounting')]"
search = "//input[@value='Class Search']"
passed = True

while(operating_system == '' and browser == ''):
    operating_system = input('Please enter your operating system (mac/win): ')
    browser = input('Please enter your browser app (chrome/firefox): ')

while(browser == 'chrome' and version == ''):
    version = input('Please enter your version of chrome (74/75/76/77): ')

while(browser == 'firefox' and version == ''):
    version = input('Please enter your version of firefox (22/23/24/25): ')

if operating_system == 'mac':
    if browser == 'chrome':
        engine = 'chromedriver'
    else:
        engine = 'geckodriver'
else:
    if browser == 'chrome':
        engine = 'chromedriver.exe'
    else:
        engine = 'geckodriver.exe'

#Set path variable    
path = r'./{}/{}/{}/{}'.format(operating_system, browser, version, engine)
print("PATH set: ", path)

#Enable driver options 
if browser == 'chrome':
    from selenium.webdriver.chrome.options import Options
else:
    from selenium.webdriver.firefox.options import Options
    
#Enable headless option (i.e. no browser window will open) - to diable this feature, change options.headless = True to options.headless = False
options = Options()
options.headless = True

print('Driver Status: Building Webdriver:', engine)
if browser == 'chrome':
    driver = webdriver.Chrome(path, options=options)
else:
    driver = webdriver.Firefox(options=options, executable_path=path)
    path = os.path.join(path, engine)

driver.get(website)
print('Driver Status: Visiting website -', website)
print('Driver Status: Finding and Clicking Schedule of Classes.')
driver.find_element_by_xpath(schedule).click()

print('Driver Status: Selecting term Spring 2019.')
driver.find_element_by_name('p_term')
driver.find_element_by_xpath(spring).click()

print('Driver Status: Submitting form.')
driver.find_element_by_xpath(select).click()

print('Driver Status: Selecting subject - Computer Science.')
driver.find_element_by_xpath(cs).click()
# driver.find_element_by_xpath(acct).click()

print('Driver Status: Submitting form.')
driver.find_element_by_xpath(search).click()

if browser == 'firefox':
    print('Driver Status: Waiting for page to load.')
    wait = WebDriverWait(driver, 60)
    wait.until(ec.visibility_of_element_located((By.CLASS_NAME, 'ddtitle')))
    print('Driver Status: Page loaded. Waiting for elements to load.')
    t.sleep(1)

print('Driver Status: Elements loaded. Finding elements.')
classes = driver.find_elements_by_class_name('ddtitle')
print('Driver Status: Elements found. Testing classes for CS.')
for title in classes:
    class_title = title.text
    # print(class_title)
    test = re.search('(CS){1}', class_title)
    if test:
        pass
    else:
        print('Test Failed! ', title.text, ' is not a CS course.')
        passed = False
        break
if passed == True:
    print('Test Passed! All courses on page are CS.')
    driver.quit()
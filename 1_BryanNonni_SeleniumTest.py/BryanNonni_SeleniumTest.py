#!/usr/bin/env python3
import os
import re
from sys import exit
from sys import argv
import time as t
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

#Declare variables
browser = ['chrome', 'firefox']
version = ['77', '25']
engine = ['chromedriver', 'geckodriver']
envs = ['./chromedriver', './geckodriver']
website = 'https://oscar.gatech.edu/'
schedule = "//*[contains(text(), 'Schedule of ')]"
spring = "//*[contains(text(), 'Spring 2019')]"
select = "//input[@value='Submit']"
cs = "//*[contains(text(), 'Computer Science')]"
#Testing failure using ACCT courses
#acct = "//*[contains(text(), 'Accounting')]"
search = "//input[@value='Class Search']"
passed = True
i = 0
H = input('Welcome to GTPylenium!\nWould you like this test to be headless (Y/n)? ')

for path in envs:
    #Set path to driver
    engine_path = path
    print("PATH set: ", path)
    if browser[i] == 'chrome':
        from selenium.webdriver.chrome.options import Options
    else:
        from selenium.webdriver.firefox.options import Options

    #Enable headless option (i.e. no browser window will open) - to diable this feature, change options.headless = True to options.headless = False
    options = Options()
    if H == 'Y':
        options.headless = True
    else:
        options.headless = False
    
    print('Driver Status: Building Webdriver')
    if browser[i] == 'chrome':
        driver = webdriver.Chrome(path, options=options)
    else:
        driver = webdriver.Firefox(options=options, executable_path=path)
        path = os.path.join(path, 'firefox')
    
    #Visit website
    driver.get(website)
    print('Driver Status: Visiting website -', website)
    
    #Find and click the Schedule of Classes link
    driver.find_element_by_xpath(schedule).click()
    print('Driver Status: Finding and Clicking Schedule of Classes.')

    #Find and click the Select Term dropdown, and select Spring 2019 option
    driver.find_element_by_name('p_term')
    driver.find_element_by_xpath(spring).click()
    
    #Find and click the Select button
    driver.find_element_by_xpath(select).click()
    print('Driver Status: Selecting term Spring 2019 & Submitting form.')

    #Find selection box and click the Computer Science option
    driver.find_element_by_xpath(cs).click()
    
    #Debugging mechanism to test accuracy of regex 
    #driver.find_element_by_xpath(acct).click()
    
    #Find and click the Search button
    driver.find_element_by_xpath(search).click()
    print('Driver Status: Selecting subject(s) & Submitting form.')

    #Conditional for firefox; geckodriver does not implicitly wait for page and elements to load unlike chrome driver
    #Conditional pauses driver using explicit wait until the class titles exist on page, then resumes driver function
    if browser == 'firefox':
        print('Driver Status: Waiting for page to load.')
        wait = WebDriverWait(driver, 60)
        wait.until(ec.visibility_of_element_located((By.CLASS_NAME, 'ddtitle')))
        print('Driver Status: Page loaded. Waiting for elements to load.')
        #Sleep gives the page an extra second to fully load all titles, geckodriver does not have this default functionality
        t.sleep(1)
        print('Driver Status: Elements loaded. Finding elements.')
    
    #Finding and getting all class titles on page
    #Try Except handles any errors on execution
    classes = driver.find_elements_by_class_name('ddtitle')
    print('Driver Status: Elements found. Testing classes for CS.')
    
    #For loop iterates through all elements returned by find_elements_by_class_name
    for title in classes:
        class_title = title.text
        #Printing titles for deubugging purposes
        #print(class_title)
        #Regex test on class title text
        test = re.search('(CS){1}', class_title)
        #If CS exists, pass, else error => Test Failed, set passed var to False, break loop execution
        if test:
            pass
        else:
            print('Test Failed! ', title.text, ' is not a CS course.')
            passed = False
            break

    #Check if test passed, print success message if True
    #If not headless, close browser window, otherwise continue outer loop to check firefox
    if passed == True:
        print(browser[i], ' Test Passed! All courses on page are CS.')
        i+=1
        if H != 'Y':
            driver.close()
        elif i == 2:
            driver.quit()
            

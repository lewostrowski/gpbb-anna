# ESSENTIAL LIBRARIES
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import datetime
import time
import os
import uuid
import json

# FRAMEWORK'S FUNCTIONS
generalErrorMessage = 'Wrong parameters'

# Start browser enginge
def startBrowser(browserUserConfig):
    if browserUserConfig.get('hideBrowserGUI') == True:
        fireFoxOptions = webdriver.FirefoxOptions()
        fireFoxOptions.headless = True
        driver = webdriver.Firefox(options=fireFoxOptions)
    else:
        driver = webdriver.Firefox()
    
    return driver

# Set wait time
def wait(secondsWait, random=False): 
    if random == False and type(secondsWait) == int:
        time.sleep(secondsWait)
    elif random == True and type(secondsWait) == list:
        if len(secondsWait) == 2: time.sleep(random.randint(secondsWait[0],secondsWait[1]))
        else: print(generalErrorMessage)
    else: print(generalErrorMessage)

# Create a logbook 
def logBook(sessionID, actionDescription, target, config, consolLog=True):
    cD = datetime.datetime.now()
    currentDate = cD.strftime(config.get('timeFormat'))
    logBooksDir = config.get('logsDirectory')
    if os.path.exists(logBooksDir) == False: os.mkdir(logBooksDir)

    if consolLog == True: print(f'{currentDate}, {actionDescription}, {target}')
    if config.get('saveLogs') == True:
        fileName = f'{logBooksDir}/{sessionID}-logbook.txt'
        if os.path.exists(fileName) != fileName: 
            logBook = open(fileName, 'w')
            logBook.write('sessionID, actionDate, actionName, actionTarget' + '\n')
            logBook.write(f'{sessionID}, {currentDate}, create logbook, {fileName}' + '\n')
        else: logBook = open(fileName, 'a')
        logBook.write(f'{sessionID}, {currentDate}, {actionDescription}, {target}'  + '\n')
        logBook.close()

# Manual testing
def requestUserAction(requestType, message=0, keyToApprove='y'):
    endRequest = False
    print('===================================')
    if requestType == 'approval':
        while endRequest != True:
            approve = input(f'{message}: ')
            if approve == keyToApprove: endRequest = True
    elif requestType == 'action':
        while endRequest != True:
            print('Provide as array:')
            print('0 to finish')
            print('1 to select and click on element')
            print('2 to write text into textarea')
            print('3 to press key')

            userInput = int(input('Action number: '))
            if userInput == 0: 
                endRequest = True
                print('===================================')
            elif userInput == 1:
                path = input('Xpath: ')
                try:
                    driver.find_element(By.XPATH, path).click()
                    print('Request: done')
                    logBook(sessionID, 'requst user action', f'Click on: {path}' , botUserConfig)
                except:
                    print('Request: fail')
                    logBook(sessionID, 'requst user action', f'Fail to click on: {path}' , botUserConfig)
                print('===================================')
            elif userInput == 2:
                try:
                    path = input('Xpath: ')
                    text = input('Text: ')
                    textbox = driver.find_element(By.XPATH, path)
                    textbox.send_keys(text)
                    print('Request: done')
                    logBook(sessionID, 'requst user action', f'Send text to: {path}' , botUserConfig)
                except:
                    print('Request: fail')
                    logBook(sessionID, 'requst user action', f'Fail to send text to: {path}' , botUserConfig)
                print('===================================')
            elif userInput == 3:
                print('Select key number:')
                print('1. Tab')
                print('2. Enter')
                keySelect = int(input('Key number: '))
                try:
                    actions = ActionChains(driver)
                    if keySelect == 1: actions.send_keys(Keys.TAB)
                    if keySelect == 2: actions.send_keys(Keys.ENTER)
                    actions.perform()
                    print('Request: done')
                    logBook(sessionID, 'requst user action', f'Press key {keySelect}' , botUserConfig)
                    print('===================================')
                except:
                    print('Request: fail')
                    logBook(sessionID, 'requst user action', f'Press key {keySelect}' , botUserConfig)
                    print('===================================')


# BOT BODY

# Import config file
with open('config.json', 'r') as jsonConfig:
    userConfig = json.load(jsonConfig)

browserUserConfig = userConfig['browserUserConfig']
botUserConfig = userConfig['botUserConfig']

# Prepare enviroment
sessionID = uuid.uuid4()
sessionStart = datetime.datetime.now()
sessionStart = sessionStart.strftime(botUserConfig.get('timeFormat'))
logBook(sessionID, f'open bot Anna session', f'session ID: {sessionID}', botUserConfig)

# Run a browrser
driver = startBrowser(browserUserConfig)
if browserUserConfig.get('getSiteAfterRun') != False: 
    driver.get(browserUserConfig.get('getSiteAfterRun'))
    logBook(sessionID, 'open site', browserUserConfig.get('getSiteAfterRun'), botUserConfig)


requestUserAction('action')









#ESSENTIAL LIBRARIES
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import datetime
import time
import os
import uuid
import json

#FRAMEWORK'S FUNCTIONS
generalErrorMessage = 'Wrong parameters'

##Start browser enginge wiht choosen option
def startBrowser(browserUserConfig):
    if browserUserConfig.get('hideBrowserGUI') == True:
        fireFoxOptions = webdriver.FirefoxOptions()
        fireFoxOptions.headless = True
        driver = webdriver.Firefox(options=fireFoxOptions)
    else:
        driver = webdriver.Firefox()
    
    return driver

##Set wait time before next action
def wait(secondsWait, random=False): 
    if random == False and type(secondsWait) == int:
        time.sleep(secondsWait)
    elif random == True and type(secondsWait) == list:
        if len(secondsWait) == 2: time.sleep(random.randint(secondsWait[0],secondsWait[1]))
        else: print(generalErrorMessage)
    else: print(generalErrorMessage)

##Create a logbook 
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

#BOT BODY

##Import config file
with open('config.json', 'r') as jsonConfig:
    userConfig = json.load(jsonConfig)

browserUserConfig = userConfig['browserUserConfig']
botUserConfig = userConfig['botUserConfig']

##Prepare enviroment
sessionID = uuid.uuid4()
sessionStart = datetime.datetime.now()
sessionStart = sessionStart.strftime(botUserConfig.get('timeFormat'))
logBook(sessionID, f'open bot Anna session', f'session ID: {sessionID}', botUserConfig)

##Run a browrser
driver = startBrowser(browserUserConfig)
if browserUserConfig.get('getSiteAfterRun') != False: 
    driver.get(browserUserConfig.get('getSiteAfterRun'))
    logBook(sessionID, 'open site', browserUserConfig.get('getSiteAfterRun'), botUserConfig)

    driver.get(browserUserConfig.get('getSiteAfterRun'))
    logBook(sessionID, 'open site', browserUserConfig.get('getSiteAfterRun'), botUserConfig)

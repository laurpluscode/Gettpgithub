from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver = webdriver.Chrome(executable_path='/Users/LaurenIT/gettopautomation/Gettpgithub/automation/chromedriver 4')

# Latest
LTEBUTTON = (By.XPATH,"//a[text() ='Latest']")

BSTSELL = (By.XPATH,"//a[text() ='Best Selling']")

MCBOOKAIR = (By.XPATH,"//a[@href='https://gettop.us/product/macbook-air/']")

MCBOOKPRO = (By.XPATH,"//a[@href='https://gettop.us/product/macbook-pro-16/']")

IPHONE_SE = (By.XPATH,"//a[@href='https://gettop.us/product/iphone-se/']")

IPHONE11 = (By.XPATH,"//a[@href='https://gettop.us/product/iphone-11']")

class LATEST:

#MACBOOKAIR
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.base_url = 'https://gettop.us/'

    def click(self, *MCBOOKAIR):
        self.driver.find_element(*MCBOOKAIR).click()

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 9)


#MACBOOKPRO

    def click(self, *MCBOOKPRO):
        self.driver.find_element(*MCBOOKPRO).click()

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 9)

#IPHONESE

    def click(self, *IPHONE_SE):
        self.driver.find_element(*IPHONE_SE).click()

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 9)

#IPHONE11

    def click(self, *IPHONE11):
        self.driver.find_element(*IPHONE11).click()

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 9)

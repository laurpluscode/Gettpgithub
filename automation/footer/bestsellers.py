from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver = webdriver.Chrome(executable_path='/Users/LaurenIT/gettopautomation/Gettpgithub/automation/chromedriver 4')

# Bestsellers
BSTSELL = (By.XPATH,"//a[text() ='Best Selling']")

MCBOOK16 = (By.XPATH,"//a[@href='https://gettop.us/product/macbook-pro-16/']")

AIRPODSPRO = (By.XPATH,"//a[@href='https://gettop.us/product/airpods-pro/']")

AIRPODS = (By.XPATH,"//a[@href='https://gettop.us/product/airpods/']")

WATCHSER3 =(By.XPATH,"//a[@href='https://gettop.us/product/land-tee-jack-jones']")

class BESTSELLERS:

#Macbook16
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.base_url = 'https://gettop.us/'

    def click(self, *MCBOOK16):
        self.driver.find_element(*MCBOOK16).click()

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 9)


#AIRPODSPRO

    def click(self, *AIRPODSPRO):
        self.driver.find_element(*AIRPODSPRO).click()

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 9)

#AIRPODS

    def click(self, *AIRPODS):
        self.driver.find_element(*AIRPODS).click()

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 9)

#WATCHSERIES3

    def click(self, *WATCHSER3):
        self.driver.find_element(*WATCHSER3).click()

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 9)

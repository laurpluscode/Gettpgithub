from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from behave import when, given, then
from time import sleep

# TOPRATED

TOPRATEBUTTON = (By.XPATH,"//a[text() ='Top rated']")


IPHONE_SE = (By.XPATH,"//a[@href='https://gettop.us/product/iphone-se/']")

AIRPODSPRO = (By.XPATH,"//a[@href='https://gettop.us/product/macbook-air/']")

AIRPODS = (By.XPATH,"//a[@href='https://gettop.us/product/airpods/']")

MCBOOK16 = (By.XPATH,"//a[@href='https://gettop.us/product/macbook-pro-16/']")

class TOPRATED:

#IPHONE_SE
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.base_url = 'https://gettop.us/'

    def click(self, *IPHONE_SE):
        self.driver.find_element(*IPHONE_SE).click()

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

    def click(self, *MCBOOK16):
        self.driver.find_element(*MCBOOK16).click()

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 9)

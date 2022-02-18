from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from behave import when, given, then
from time import sleep

BCKTOPBUTTON = (By.XPATH,"//a[@href='#top']")


class BACK2TOP:

#BACK2TOP
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.base_url = 'https://gettop.us/'

    def click(self, *BCKTOPBUTTON):
        self.driver.find_element(*BCKTOPBUTTON).click()

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 9)

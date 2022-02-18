from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver = webdriver.Chrome(executable_path='/Users/LaurenIT/gettopautomation/Gettpgithub/automation/chromedriver 4')


CPYRGHT2022 = (By.XPATH,"//a [@class='copyright-footer']")

class Copyright2022:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.base_url = 'https://gettop.us/'

    def click(self, *CPYRGHT2022):
        self.driver.find_element(*CPYRGHT2022).click()

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 9)

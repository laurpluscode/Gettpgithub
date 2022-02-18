from time import sleep

from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

LTEBUTTON = (By.XPATH,"//a[text() ='Latest']")

MCBOOKAIR = (By.XPATH,"//a[@href='https://gettop.us/product/macbook-air/']")

MCBOOKPRO = (By.XPATH,"//a[@href='https://gettop.us/product/macbook-pro-16/']")

IPHONE_SE = (By.XPATH,"//a[@href='https://gettop.us/product/iphone-se/']")

IPHONE11 = (By.XPATH,"//a[@href='https://gettop.us/product/iphone-11']")

@given('Open Gettop page')
def open_gettop(context):
    context.driver.get('https://gettop.us/')
    context.app.main_page.open()

@when('User is at the footer of the homepage')
def open_gettoppage(context):
    context.driver.get('https://gettop.us/')


@then('Verify if link one is Macbookair')
def verify_Best_selling(context):
    context.driver.find_element(*MCBOOKAIR ).click()
    sleep(1)


@then('Verify if link two is Macbook Pro')
def verify_Latest(context):
    context.driver.find_element(*MCBOOKPRO).click()
    sleep(1)


@then('Verify if link three is iPhone SE')
def verify_Top_rated(context):
    context.driver.find_element(*IPHONE_SE).click()
    sleep(1)


@then('Verify if link three is iPhone 11')
def verify_Top_rated(context):
    context.driver.find_element(*IPHONE11).click()
    sleep(1)
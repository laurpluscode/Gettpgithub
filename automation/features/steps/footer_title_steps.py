from time import sleep

from selenium.webdriver.common.by import By
from behave import given, when, then

BSTSELL = (By.XPATH, "//a[text() ='Best Selling']")
TOPRATEBUTTON = (By.XPATH, "//a[text() ='Top rated']")
LTEBUTTON = (By.XPATH, "//a[text() ='Latest']")


@given('Open Gettop page')
def open_gettop(context):
    context.driver.get('https://gettop.us/')
    context.app.main_page.open()


@when('User is at the footer of the homepage')
def open_gettoppage(context):
    context.driver.get('https://gettop.us/')


@then('Verify if link one is Best selling')
def verify_best_selling(context):
    context.driver.find_element(*BSTSELL).click()
    sleep(1)


@then('Verify if link two is Latest')
def verify_latest(context):
    context.driver.find_element(*LTEBUTTON).click()
    sleep(1)


@then('Verify if link three is Top rated')
def verify_top_rated(context):
    context.driver.find_element(*TOPRATEBUTTON).click()
    sleep(1)

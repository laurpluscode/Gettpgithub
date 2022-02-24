from time import sleep

from selenium.webdriver.common.by import By
from behave import given, when, then

# Bestsellers
MCBOOK16 = (By.XPATH, "//a[@href='https://gettop.us/product/macbook-pro-16/']")

AIRPODSPRO = (By.XPATH, "//a[@href='https://gettop.us/product/airpods-pro/']")

AIRPODS = (By.XPATH, "//a[@href='https://gettop.us/product/airpods/']")

WATCHSER3 = (By.XPATH, "//a[@href='https://gettop.us/product/land-tee-jack-jones']")


@given('Open Gettop page')
def open_gettop(context):
    context.driver.get('https://gettop.us/')
    context.app.main_page.open()


@when('User is at the footer of the homepage')
def open_gettoppage(context):
    context.driver.get('https://gettop.us/')


@then('Verify if link one is macbook 16')
def verify_best_selling(context):
    context.driver.find_element(*MCBOOK16).click()
    sleep(1)


@then('Verify if link two is airpodspro')
def verify_latest(context):
    context.driver.find_element(*AIRPODSPRO).click()
    sleep(1)


@then('Verify if link two is airpods')
def verify_atest(context):
    context.driver.find_element(*AIRPODS).click()
    sleep(1)


@then('Verify if link three is watch series 3')
def verify_Top_rated(context):
    context.driver.find_element(*WATCHSER3).click()
    sleep(1)

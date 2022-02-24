from time import sleep

from selenium.webdriver.common.by import By
from behave import given, when, then

# Products
MCBOOK16 = (By.XPATH, "//a[@href='https://gettop.us/product/macbook-pro-16/']")

MCBOOK13 = (By.XPATH, "//a[@href='https://gettop.us/product/macbook-pro-13/']")

MCBOOKAIR = (By.XPATH, "//a[@href='https://gettop.us/product/macbook-air/']")

AIRPODSPRO = (By.XPATH, "//a[@href='https://gettop.us/product/airpods-pro/']")

AIRPODS = (By.XPATH, "//a[@href='https://gettop.us/product/airpods/']")

WATCHSER3 = (By.XPATH, "//a[@href='https://gettop.us/product/land-tee-jack-jones']")

IPAD = (By.XPATH, "//a[@href='https://gettop.us/product/ipad/']")

IPADAIR = (By.XPATH, "//a[@href='https://gettop.us/product/ipad-air/']")

IPADMINI = (By.XPATH, "//a[@href='https://gettop.us/product/ipad-mini/']")

IPADPRO = (By.XPATH, "//a[@href='https://gettop.us/product/ipad-pro/']")

WATCHSER5 = (By.XPATH, "//a[@href='https://gettop.us/product/ss-crew-california-sub-river-island/']")

IPHONE_SE = (By.XPATH, "//a[@href='https://gettop.us/product/iphone-se/']")

IPHONE11 = (By.XPATH, "//a[@href='https://gettop.us/product/iphone-11']")

IPHONE11PRO = (By.XPATH, "//a[@href='https://gettop.us/product/iphone-11pro']")


@given('Open Gettop page')
def open_gettop(context):
    context.driver.get('https://gettop.us/')
    context.app.main_page.open()


@when('User is at the footer of the homepage')
def open_gettoppage(context):
    context.driver.get('https://gettop.us/')


@then('Verify if link one is macbook 16')
def verify_macbook_16(context):
    context.driver.find_element(*MCBOOK16).click()
    sleep(1)


@then('Verify if link two is airpodspro')
def verify_airpodspro(context):
    context.driver.find_element(*AIRPODSPRO).click()
    sleep(1)


@then('Verify if link three is airpods')
def verify_airpods(context):
    context.driver.find_element(*AIRPODS).click()
    sleep(1)


@then('Verify if link four is watch series 3')
def verify_watch_series_3(context):
    context.driver.find_element(*WATCHSER3).click()
    sleep(1)


@then('Verify if link five is macbook 13')
def verify_macbook_13(context):
    context.driver.find_element(*MCBOOK13).click()
    sleep(1)


@then('Verify if link six is macbook air')
def verify_macbook_air(context):
    context.driver.find_element(*MCBOOKAIR).click()
    sleep(1)


@then('Verify if link seven is ipad')
def verify_ipad(context):
    context.driver.find_element(*IPAD).click()
    sleep(1)


@then('Verify if link eight is ipad air')
def verify_ipad_air(context):
    context.driver.find_element(*IPADAIR).click()
    sleep(1)


@then('Verify if link nine is ipad mini')
def verify_ipad_mini(context):
    context.driver.find_element(*IPADMINI).click()
    sleep(1)


@then('Verify if link ten is iphone 11')
def verify_iphone_11(context):
    context.driver.find_element(*IPHONE11).click()
    sleep(1)


@then('Verify if link eleven is iphone 11 pro')
def verify_iphone_11_pro(context):
    context.driver.find_element(*IPHONE11PRO).click()
    sleep(1)


@then('Verify if link tweleve is watch series 5')
def verify_watch_series_5(context):
    context.driver.find_element(*WATCHSER5).click()
    sleep(1)


@then('Verify if link thirteen is IPADPRO')
def verify_IPADPRO(context):
    context.driver.find_element(*IPADPRO).click()
    sleep(1)


@then('Verify if link fourteen is iphone se')
def verify_iphone_se(context):
    context.driver.find_element(*IPHONE_SE).click()
    sleep(1)

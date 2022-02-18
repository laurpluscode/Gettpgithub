from time import sleep

from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

TOPRATEBUTTON = (By.XPATH,"//a[text() ='Top rated']")

ANIME_MENU = (By.ID, 'nav-anime-menu')
FOOTER_LINKS = (By.CSS_SELECTOR, "td.navFooterDescItem a")
SIGN_IN_BTN = (By.CSS_SELECTOR, "#nav-signin-tooltip a.nav-action-button")

@given('Open Gettop page')
def open_gettop(context):
    context.driver.get('https://gettop.us/')
    context.app.main_page.open()

@when('User is at the footer of the homepage')
def open_gettoppage(context):
    context.driver.get('https://gettop.us/')


@And('Verify if link one is Best selling')
def verify_Best_selling(context):
    context.driver.find_element(*BSTSELL).click()
    sleep(1)


@And('Verify if link two is Latest')
def verify_Latest(context):
    context.driver.find_element(*LTEBUTTON).click()
    sleep(1)


@Then('Verify if link three is Top rated')
def verify_Top_rated(context):
    context.driver.find_element(*TOPRATEBUTTON).click()
    sleep(1)
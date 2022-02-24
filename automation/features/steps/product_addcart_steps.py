from behave import when, then
from selenium.webdriver.common.by import By

CART = (By.XPATH, "//a [@href= 'https://gettop.us/cart/']")
VIEW_CART = (By.ID, "//a[@class='button wc-forward']")
ADDCART = (By.ID, "//a[@class='single_add_to_cart_button button alt']")
CATEGORYMACPRO = (By.ID, "//a[@href='https://gettop.us/product-category/macbook/']")
XBUTTON = (By.ID, "//a[@class ='mfp-close']")
PRODUCT = (By.XPATH, "//a [@class ='woocommerce-mini-cart-item mini_cart_item']")
PRODUCT_NAME = (By.XPATH, "// a[@class ='name product-title']")


@when('Open cart page')
def open_cart_page(context):
    context.driver.get('https://www.gettop.us/gp/cart/view.html?ref_=nav_cart')


@then('Verify cart has {expected_count} item(s)')
def verify_cart_count(context, expected_count):
    actual_count = context.driver.find_element(*CART).text
    assert actual_count == expected_count, f'Error, actual {actual_count} did not match {expected_count}'
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()


@then('Verify cart has correct product')
def verify_product_name(context):
    actual_name = context.driver.find_element(*PRODUCT_NAME).text
    assert context.product_name[:30] in actual_name, f'Expected {context.product_name}but go'

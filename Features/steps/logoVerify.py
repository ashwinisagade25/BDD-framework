from selenium import webdriver
from behave import *

@given('Launch chrome browser')
def launchbrowser(context):
    context.driver=webdriver.Chrome()

@when('open homepage')
def openhomepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@then('logo is present')
def verifylogo(context):
    status=context.driver.find_element_by_css_selector("div#divLogo img").is_displayed()
    assert status==True

@then('close browser')
def closebrowser(context):
    context.driver.close()

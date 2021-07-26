import time
from selenium import webdriver
from behave import *
import allure
from allure_commons.types import AttachmentType

@when('Enter username "{username}" and Paswword "{password}"')
def enterlogindata(context,username,password):
    context.driver.find_element_by_id("txtUsername").send_keys(username)
    context.driver.find_element_by_id("txtPassword").send_keys(password)

@when('click on login button')
def clicklogin(context):
    context.driver.find_element_by_id("btnLogin").click()

@then('user must successfully login to dashboard page')
def verifylogin(context):
    time.sleep(2)
    status = context.driver.find_element_by_css_selector("div.head h1").is_displayed()
    allure.attach(context.driver.get_screenshot_as_png(),
                  name="invalid",
                  attachment_type=AttachmentType.PNG)
    assert status == True

@then(u'user must see error msg')
def Verifyerrormsg(context):
    status = context.driver.find_element_by_css_selector("div#divLoginButton span").is_displayed()
    time.sleep(2)
    assert status == True





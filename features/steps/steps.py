from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


chromedriver_path = "/Users/grant/Desktop/noipcoding/forceQA/forceautoqa/rsc/chromedriver"
driver = webdriver.Chrome(chromedriver_path)
driver.get("https://test.salesforce.com")

@given('user with invalid credential')
def step_impl(context):
    username = driver.find_element_by_id("username")
    password = driver.find_element_by_id("password")
    username.send_keys("wrong@wrong.com")
    password.send_keys("Pa55worD")
    driver.find_element_by_id("Login").click()


@then('user cannot log in')
def step_impl(context):
    assert context.failed is False
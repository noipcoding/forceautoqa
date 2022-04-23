from selenium import webdriver
from selenium.webdriver.common.keys import Keys




def open_browser(browser_type):
    chromedriver_path = "/Users/grant/Desktop/noipcoding/forceQA/forceautoqa/rsc/chromedriver"
    driver = webdriver.Chrome(chromedriver_path)
    driver.get("https://test.salesforce.com")



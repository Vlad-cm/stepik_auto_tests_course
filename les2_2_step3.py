from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math


try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = int(browser.find_element(By.CSS_SELECTOR, "span[id='num1']").text)
    num2 = int(browser.find_element(By.CSS_SELECTOR, "span[id='num2']").text)
    x = num1 + num2
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(x))

    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

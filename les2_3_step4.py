from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


link = "http://suninjuly.github.io/alert_accept.html"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    btn1 = browser.find_element(By.TAG_NAME, "button")
    btn1.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element(By.CSS_SELECTOR, "span[id='input_value']")
    x = x_element.text
    y = calc(x)
    input_field = browser.find_element(By.CSS_SELECTOR, "input[id='answer']")
    input_field.send_keys(y)

    btn2 = browser.find_element(By.TAG_NAME, "button")
    btn2.click()
finally:
    time.sleep(15)
    browser.quit()

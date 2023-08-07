import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit'")
    button.click()

    alert = browser.switch_to.alert
    alert.accept()

    number = browser.find_element(By.CSS_SELECTOR, "span#input_value")
    number_value = int(number.text)

    result = math.log(abs(12*math.sin(number_value)))

    input_answer = browser.find_element(By.CSS_SELECTOR, "input#answer")
    input_answer.send_keys(result)

    submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

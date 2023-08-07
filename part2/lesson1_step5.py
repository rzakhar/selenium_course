import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "span#input_value")
    x = x_element.text
    y = calc(x)
    input_answer = browser.find_element(By.CSS_SELECTOR, "input#answer")
    input_answer.send_keys(y)

    checkbox = browser.find_element(By.CSS_SELECTOR, "label[for='robotCheckbox'")
    checkbox.click()

    radiobutton = browser.find_element(By.CSS_SELECTOR, "label[for='robotsRule'")
    radiobutton.click()

    submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

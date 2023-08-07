import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 12).until(
        ec.text_to_be_present_in_element((By.CSS_SELECTOR, "h5#price"), "$100")
    )

    book = browser.find_element(By.CSS_SELECTOR, "button#book")
    book.click()

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

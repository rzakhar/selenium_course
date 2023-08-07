import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_number = browser.find_element(By.CSS_SELECTOR, "span#num1")
    first_number_value = first_number.text

    second_number = browser.find_element(By.CSS_SELECTOR, "span#num2")
    second_number_value = second_number.text

    result = int(first_number_value) + int(second_number_value)

    select = Select(browser.find_element(By.CSS_SELECTOR, "select#dropdown"))
    select.select_by_value(str(result))  # ищем элемент с текстом
    
    submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

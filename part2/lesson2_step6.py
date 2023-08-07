import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    number = browser.find_element(By.CSS_SELECTOR, "span#input_value")
    number_value = int(number.text)

    result = math.log(abs(12*math.sin(number_value)))

    input_answer = browser.find_element(By.CSS_SELECTOR, "input#answer")
    input_answer.send_keys(result)
    
    checkbox = browser.find_element(By.CSS_SELECTOR, "label[for='robotCheckbox'")
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
    checkbox.click()

    radiobutton = browser.find_element(By.CSS_SELECTOR, "label[for='robotsRule'")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
    radiobutton.click()

    submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

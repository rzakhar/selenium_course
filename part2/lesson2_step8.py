import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.CSS_SELECTOR, "input[name='firstname'")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, "input[name='lastname'")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, "input[name='email'")
    input3.send_keys("ivan@petrov.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')

    input_file = browser.find_element(By.CSS_SELECTOR, "input#file")
    input_file.send_keys(file_path)

    submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

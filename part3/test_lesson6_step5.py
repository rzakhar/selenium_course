import pytest
import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestAlienMessage:
    links = ['https://stepik.org/lesson/236895/step/1',
             'https://stepik.org/lesson/236896/step/1',
             'https://stepik.org/lesson/236897/step/1',
             'https://stepik.org/lesson/236898/step/1',
             'https://stepik.org/lesson/236899/step/1',
             'https://stepik.org/lesson/236903/step/1',
             'https://stepik.org/lesson/236904/step/1',
             'https://stepik.org/lesson/236905/step/1']

    @pytest.mark.parametrize('link', links)
    def test_get_alien_message(self, browser, link):
        # open page
        browser.get(link)

        # login
        login_button = WebDriverWait(browser, 20).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "a.navbar__auth_login"))
        )

        login_button.click()

        email_input = browser.find_element(By.CSS_SELECTOR, "input#id_login_email")
        email_input.send_keys('romanzakharov329@gmail.com')

        password_input = browser.find_element(By.CSS_SELECTOR, "input#id_login_password")
        password_input.send_keys('')

        submit_login_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_login_button.click()

        user_avatar = WebDriverWait(browser, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "img.navbar__profile-img"))
        )

        # enter answer
        answer_input = WebDriverWait(browser, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "textarea.string-quiz__textarea"))
        )

        if len(browser.find_elements(By.CSS_SELECTOR, "button.again-btn")) == 0:
            answer_input.send_keys(str(math.log(int(time.time()))))

            # send
            answer_submit = browser.find_element(By.CSS_SELECTOR, "button.submit-submission")
            answer_submit.click()

        # wait for the feedback
        lesson_hint = WebDriverWait(browser, 30).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "p.smart-hints__hint"))
        )

        # check the feedback
        hint = lesson_hint.text
        assert hint == 'Correct!', \
            f"expected {'Correct'}, got {'hint'}"

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_find_add_card_button(browser):
    browser.get(link)
    try:
        browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
        present_elem = True
    except:
        present_elem = False
    assert present_elem, "No add_card button on page"

# pytest --language=es test_items.py
# команды для проверки:
# import time           в начало
# time.sleep(30)        после browser.get

# страница с ошибкой для проверки assert: 
# http://selenium1py.pythonanywhere.com/catalogue/oscar-t-shirt_1/

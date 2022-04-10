import pytest
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def check_exists_by_css():
    try:
        browser.find_element_by_css_selector("button.btn-add-to-basket")
    except NoSuchElementException:
        return False
    return True

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    #раскомментируйте следующую строку для проверки корректности отображения языка:
    #time.sleep(30)    
    assert check_exists_by_css!=True, "There is no button on page."

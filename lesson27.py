from selenium import webdriver
import time
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(x))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)
    
    bn = browser.find_element_by_tag_name("button");
    bn.click()
    
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)  
    
    x_value = browser.find_element_by_css_selector("span#input_value");
    x = int(x_value.text)
    y = math.log(abs(12*math.sin(x)))
    
    ans = browser.find_element_by_css_selector("input#answer")        
    ans.send_keys(str(y))
    
    button = browser.find_element_by_css_selector("button")
    button.click()
    time.sleep(5)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


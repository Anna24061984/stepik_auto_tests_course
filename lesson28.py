from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    # говорим WebDriver ждать все элементы в течение 5 секунд
    #browser.implicitly_wait(5)

    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    
    button = WebDriverWait(browser, 13).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"$100")
    )
    
    button = browser.find_element_by_id("book")
    button.click()
    
    x_element = browser.find_element_by_css_selector('span[id="input_value"]')
    x = int(x_element.text)    
    z = calc(x)        
    
    t = browser.find_element_by_id("answer")
    t.send_keys(str(z))

    bt = browser.find_element_by_id("solve")    
    bt.click()
    
    time.sleep(10)
finally:    
    # закрываем браузер после всех манипуляций
    browser.quit()
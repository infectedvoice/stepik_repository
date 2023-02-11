from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Складываем числа
    num1 = browser.find_element(By.CSS_SELECTOR, "#num1")
    num1_value = num1.text
    num2 = browser.find_element(By.CSS_SELECTOR, "#num2")
    num2_value = num2.text
    summ=int(num1_value)+int(num2_value)

    # Выбираем ответ и нажимаем кнопку
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(str(summ))
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

   
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
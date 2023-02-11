from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    valuex = browser.find_element(By.CSS_SELECTOR, "#treasure")
    x = valuex.get_attribute("valuex")
    y = calc(x)

    # Отправляем заполненную форму

    checkbox=browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox.click()
    radiobutton=browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radiobutton.click()
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

   
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
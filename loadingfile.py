from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, "body > div > form > div > input:nth-child(4)")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, "div > input:nth-child(6)")
    input3.send_keys("fake@fake.com")
    input4 = browser.find_element(By.CSS_SELECTOR, "#file")
    file_path = os.path.join("H:\Infected Voice\environments\selenium_course", 'cv.txt')
    input4.send_keys(file_path)


    # Отправляем заполненную форму
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
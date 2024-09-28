import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Путь к Chrome и ChromeDriver
chrome_bin = os.environ.get("GOOGLE_CHROME_BIN", "/usr/bin/google-chrome")
chrome_driver_path = os.environ.get("CHROMEDRIVER_PATH", "/usr/bin/chromedriver")

# Опции для headless режима
chrome_options = Options()
chrome_options.binary_location = chrome_bin
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Запускаем браузер
driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)

# Открываем Google и выполняем поиск
driver.get("https://www.google.com")
time.sleep(3)

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium WebDriver")
search_box.submit()

time.sleep(3)

# Ищем второй результат
results = driver.find_elements(By.TAG_NAME, "h3")
if len(results) > 1:
    second_result_title = results[1].text
    print("Название второго сайта в поисковой выдаче:", second_result_title)
else:
    print("Не найдено достаточное количество результатов.")

# Закрываем браузер
driver.quit()

import pytest
import time
from selenium import webdriver

#Подставьте сюда свой путь до веб-драйвера
driver_path = r'chromedriver_mac64.exec'

@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options, executable_path=driver_path)
    driver.get("https://b2c.passport.rt.ru")
    time.sleep(6)
    return driver
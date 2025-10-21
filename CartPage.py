import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 4)

    @allure.step("Перейти в корзину")
    def go_to_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, '.rt03pf0').click()
    

    def clear_cart(self):
        self.driver.find_element(By.CSS_SELECTOR,   ....   ).click()
        self.driver.find_element(By.CSS_SELECTOR,    ....).click()

    def 
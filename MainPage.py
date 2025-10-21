import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 4)

    @allure.step("Открытие сайта Деливери")
    def open(self):
        self.driver.get("https://market-delivery.yandex.ru")

    @allure.severity("Выбор магазина")
    def choose_a_store(self):
        self.driver.find_element(By.CSS_SELECTOR, ".ckb1wui").click()

    @allure.step("Добавить товар в корзину")
    def add_item_to_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, '[role="presentation"]').click()

    @allure.step("Проверяем, что счетчик товара увеличился на 1")
    def result(self):
        container = self.driver.find_element(By.CSS_SELECTOR, ".UiKitProductCardRow_counterWrapper")
        fields = self.driver.find_element(By.CSS_SELECTOR, "label")
        res = self.driver.find_element(By.CSS_SELECTOR, "div").text
        
        assert res == 1
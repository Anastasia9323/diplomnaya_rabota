import allure
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShopPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Добавить товар в корзину")
    def add_item_to_cart(self):
        items = self.driver.find_elements(
            By.CSS_SELECTOR, '[aria-label="В корзину"]')
        if items:
            items[0].click()
            self.wait.until(
                EC.presence_of_element_located((
                    By.CSS_SELECTOR, '[aria-label*="Увеличить"]'))
            )
            time.sleep(1)

    @allure.step("Получение счетчика")
    def result(self):
        counters = self.driver.find_elements(By.XPATH, '//span[text()>0]')
        if len(counters) > 1:
            counter = counters[1]
        else:
            counter = counters[0] if counters else None
        return counter.text if counter else "0"

    @allure.step("Увеличение количества товара на {n} раз")
    def item_increase(self, n):
        for i in range(n):
            btn = self.wait.until(
                EC.element_to_be_clickable((
                    By.CSS_SELECTOR, '[aria-label*="Увеличить"]'))
            )
            self.driver.execute_script("arguments[0].click();", btn)
            time.sleep(0.5)
            self.wait.until(
                EC.element_to_be_clickable((
                    By.CSS_SELECTOR, '[aria-label*="Увеличить"]'))
            )

    @allure.step("Уменьшение количества товара на {n} раз")
    def item_decrease(self, n):
        for i in range(n):
            btn = self.wait.until(
                EC.element_to_be_clickable((
                    By.CSS_SELECTOR, '[aria-label*="Уменьшить"]'))
            )
            self.driver.execute_script("arguments[0].click();", btn)
            time.sleep(0.5)
            self.wait.until(
                EC.element_to_be_clickable((
                    By.CSS_SELECTOR, '[aria-label*="Уменьшить"]'))
            )

    @allure.step("Очистка корзины")
    def clear_cart(self):
        clear_btn = self.wait.until(
            EC.element_to_be_clickable((
                By.XPATH, '//button[.//span[text()="Очистить"]]'))
        )
        clear_btn.click()

        confirm_btn = self.wait.until(
            EC.element_to_be_clickable((
                By.XPATH, '//button[.//span[text()="Да, очистить"]]'))
        )
        confirm_btn.click()

        self.wait.until(
            lambda driver: self.result() == "0" or self.check_cart_is_empty()
        )

    @allure.step("Проверка что корзина пуста")
    def check_cart_is_empty(self):
        empty_cart_text = self.wait.until(
            EC.visibility_of_element_located((
                By.XPATH, '//h3[contains(text(), "пока пусто")]'))
        )
        return empty_cart_text.is_displayed()

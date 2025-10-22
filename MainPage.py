import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.driver.delete_all_cookies()

    @allure.step("Открытие сайта Деливери Омск")
    def open(self):
        self.driver.get("https://market-delivery.yandex.ru/omsk?shippingType=delivery")

    @allure.severity("Выбор магазина")
    def choose_a_store(self):
        self.driver.find_element(By.CSS_SELECTOR, ".ckb1wui").click()

    @allure.step("Добавить товар в корзину")
    def add_item_to_cart(self):
        items = self.driver.find_elements(
            By.CSS_SELECTOR, '[aria-label="В корзину"]')
        if items:
            items[0].click()

    @allure.step("Ввод адреса")
    def add_address(self):
        self.driver.find_element(By.CSS_SELECTOR, '.s1v4x2t8').click()
        address_input = self.driver.find_element(
            By.CSS_SELECTOR, '[data-testid="address-input"]')
        address_input.send_keys("Светловская, 6")
        address_input.send_keys(Keys.RETURN)
        self.driver.find_element(By.CSS_SELECTOR, '.o16sqpc5').click()

    @allure.step("Получение счетчика")
    def result(self):
        counters = self.driver.find_elements(By.XPATH, '//span[text()>0]')
        print(counters)
        if len(counters) > 1:
            counter = counters[1]
            return counter.text
    
    @allure.step("Уменьшение количества товара")
    def item_decrease(self):
        self.driver.find_element(
            By.CSS_SELECTOR, '[aria-label="Уменьшить"]').click()

    @allure.step("Увеличение количества товара")
    def item_increase(self):
        self.driver.find_element(
            By.CSS_SELECTOR, '[aria-label="Увеличить"]').click()
        
    


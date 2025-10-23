import allure
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открытие сайта Деливери Омск")
    def open(self):
        self.driver.get(self.url)

    @allure.step("Получение заголовка страницы")
    def get_title(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.title and len(driver.title) > 20
        )
        return self.driver.title

    @allure.step("Получение заголовков на странице")
    def get_main_headers(self):
        try:
            WebDriverWait(self.driver, 10).until(
                lambda driver: len(driver.find_elements(
                    By.XPATH, '//div//h2')) >= 4
            )
        except TimeoutException:
            # Если не нашли 4 заголовка, возвращаем то что есть
            header_elements = self.driver.find_elements(By.XPATH, '//div//h2')
            header_texts = [header.text for header in header_elements if header.text.strip()]
            return header_texts

        header_elements = self.driver.find_elements(By.XPATH, '//div//h2')
        header_texts = [header.text for header in header_elements if header.text.strip()]
        return header_texts

    @allure.step("Проверка и установка адреса")
    def add_address(self, address="Светловская, 6"):
        # Проверяем есть ли кнопка "Да" и кликаем если есть
        yes_buttons = self.driver.find_elements(
            By.XPATH, '//button[.//span[text()="Да"]]')
        if yes_buttons:
            yes_buttons[0].click()

        # Если адрес не отображается - устанавливаем
        if not self.driver.find_elements(By.CSS_SELECTOR, '.f18sb35s'):
            self.driver.find_element(By.CSS_SELECTOR, '.s1v4x2t8').click()
            address_input = self.driver.find_element(
                By.CSS_SELECTOR, '[data-testid="address-input"]')
            address_input.clear()
            address_input.send_keys(address)
            address_input.send_keys(Keys.RETURN)
            self.driver.find_element(By.CSS_SELECTOR, '.o16sqpc5').click()

    @allure.step("Выбор магазина")
    def choose_store(self, name):
        # Ждем загрузки магазинов
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, '[data-place-slug]'))
        )

        # Ищем все элементы с текстом "Магнит" в названии
        magnit_stores = self.driver.find_elements(
            By.XPATH, f'//a[contains(@aria-label, "{name}")]'
        )
        store_element = magnit_stores[0]

        if magnit_stores:
            # Кликаем на первый найденный Магнит
            self.driver.execute_script("arguments[0].click();", store_element)
        else:
            # Если не нашли Магнит, кидаем ошибку
            raise Exception("Магазин Магнит не найден")

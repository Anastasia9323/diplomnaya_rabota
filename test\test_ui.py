import pytest
import allure
from selenium import webdriver
from MainPage import MainPage
from CartPage import CartPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_cart(driver):
    main_page = MainPage(driver)

    with allure.step("Открытие сайта Деливери"):
        main_page.open()

    with allure.step("Выбор магазина"):
        main_page.choose_a_store()

    with allure.step("Добавить товар в корзину"):
        main_page.add_item_to_cart()

    with allure.step("Проверяем, что счетчик товара увеличился на 1"):
        main_page.result()


def test_clear_cart(driver):
    cart_page = CartPage(driver)

    with allure.step("Добавить товар в корзину"):
        test_cart()

    with allure.step("Перейти в корзину"):
        cart_page.go_to_cart()

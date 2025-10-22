import pytest
import allure
from selenium import webdriver
from MainPage import MainPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_cart(driver):
    main_page = MainPage(driver)

    with allure.step("Открытие сайта Деливери Омск"):
        main_page.open()

    with allure.step("Ввод адреса"):
        main_page.add_address()

    with allure.step("Выбор магазина"):
        main_page.choose_a_store()

    with allure.step("Добавить товар в корзину"):
        main_page.add_item_to_cart()

    with allure.step("Получение счетчика"):
        res = main_page.result()
        assert res == 1


def test_item_increase(driver):
    main_page = MainPage(driver)
    with allure.step("Открытие сайта Деливери Омск"):
        main_page.open()

    with allure.step("Ввод адреса"):
        main_page.add_address()

    with allure.step("Выбор магазина"):
        main_page.choose_a_store()

    with allure.step("Добавить товар в корзину"):
        main_page.add_item_to_cart()

    with allure.step("Увеличение количества товара"):
        main_page.item_increase()

    with allure.step("Получение счетчика"):
        res = main_page.result()
        assert res == 2

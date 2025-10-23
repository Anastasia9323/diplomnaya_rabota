import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.main_page import MainPage
from pages.shop_page import ShopPage
from config import BASE_URL, MAIN_TITLE, EXPECTED_HEADERS


@pytest.fixture
def driver():
    options = Options()
    options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.geolocation": 1,
    })
    driver = webdriver.Chrome(options=options)
    omsk_location = {
        "latitude": 54.988,
        "longitude": 73.368,
        "accuracy": 100
    }

    driver.execute_cdp_cmd("Emulation.setGeolocationOverride", omsk_location)

    driver.implicitly_wait(20)
    driver.maximize_window()

    yield driver
    driver.quit()


@allure.title("Проверка основного заголовка")
@allure.severity(allure.severity_level.CRITICAL)
def test_check_main_title(driver):
    main_page = MainPage(driver, BASE_URL)

    with allure.step("Открытие сайта Деливери Омск"):
        main_page.open()

    with allure.step("Ввод адреса"):
        actual_title = main_page.get_title()
        assert actual_title == MAIN_TITLE, \
            f"Заголовок страницы не совпадает. Ожидалось: '{MAIN_TITLE}', Фактический: '{actual_title}'"


@allure.title("Проверка заголовка главной страницы")
@allure.severity(allure.severity_level.CRITICAL)
def test_check_main_page_headers(driver):
    main_page = MainPage(driver, BASE_URL)

    with allure.step("Открытие главной страницы"):
        main_page.open()

    with allure.step("Получение заголовков разделов"):
        actual_headers = main_page.get_main_headers()

    with allure.step("Сравнение с ожидаемыми заголовками"):
        for expected_header in EXPECTED_HEADERS:
            assert expected_header in actual_headers, f"Заголовок '{expected_header}' не найден. Найдены: {actual_headers}"


@allure.title("Проверка на добавление товара в козину")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_to_cart(driver):
    main_page = MainPage(driver, BASE_URL)

    with allure.step("Открытие сайта Деливери Омск"):
        main_page.open()

    with allure.step("Ввод адреса"):
        main_page.add_address()

    with allure.step("Выбор магазина"):
        main_page.choose_store("Магнит")

    shop_page = ShopPage(driver)

    with allure.step("Добавить товар в корзину"):
        shop_page.add_item_to_cart()

    with allure.step("Получение счетчика"):
        res = shop_page.result()
        assert res == "1"


@allure.title("Проверка на увеличение количества товаров в корзине")
@allure.severity(allure.severity_level.CRITICAL)
def test_increase_item_in_cart(driver):
    main_page = MainPage(driver, BASE_URL)

    with allure.step("Открытие сайта Деливери Омск"):
        main_page.open()

    with allure.step("Ввод адреса"):
        main_page.add_address()

    with allure.step("Выбор магазина"):
        main_page.choose_store("Магнит")

    shop_page = ShopPage(driver)

    with allure.step("Добавить товар в корзину"):
        shop_page.add_item_to_cart()

    with allure.step("Увеличение количества товара"):
        shop_page.item_increase(2)

    with allure.step("Получение счетчика"):
        res = shop_page.result()
        print(f"Финальное значение счетчика: {res}")
        assert res == "2", f"Ожидалось '2', но получено '{res}'"


@allure.title("Проверка на уменьшение количества товаров в корзине")
@allure.severity(allure.severity_level.CRITICAL)
def test_decrease_item_in_cart(driver):
    main_page = MainPage(driver, BASE_URL)

    with allure.step("Открытие сайта Деливери Омск"):
        main_page.open()

    with allure.step("Ввод адреса"):
        main_page.add_address()

    with allure.step("Выбор магазина"):
        main_page.choose_store("Магнит")

    shop_page = ShopPage(driver)

    with allure.step("Добавить товар в корзину"):
        shop_page.add_item_to_cart()

    with allure.step("Увеличение количества товара"):
        shop_page.item_increase(3)

    with allure.step("Уменьшение количества товара"):
        shop_page.item_decrease(1)

    with allure.step("Получение счетчика"):
        res = shop_page.result()
        print(f"Финальное значение счетчика: {res}")
        assert res == "2", f"Ожидалось '2', но получено '{res}'"


@allure.title("Проверка на добавление и очистки корзины")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_and_clear_cart(driver):
    main_page = MainPage(driver, BASE_URL)

    with allure.step("Открытие сайта Деливери Омск"):
        main_page.open()

    with allure.step("Ввод адреса"):
        main_page.add_address()

    with allure.step("Выбор магазина"):
        main_page.choose_store("Магнит")

    shop_page = ShopPage(driver)

    with allure.step("Добавить товар в корзину"):
        shop_page.add_item_to_cart()

    with allure.step("Получение счетчика"):
        shop_page.clear_cart()

    with allure.step("Получение счетчика"):
        assert shop_page.check_cart_is_empty()

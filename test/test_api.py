import pytest
from api.search_api import SearchAPI


@pytest.fixture
def api():
    return SearchAPI()


@pytest.mark.parametrize("product,city,longitude,latitude", [
    ("молоко", "Омск", 73.46727297021081, 54.89559112123436),
    ("вода", "Москва", 37.617698, 55.755864),
    ("сок", "СПб", 30.315868, 59.939095),
])
def test_search_in_russian(api, product, city, longitude, latitude):
    location = {
        "longitude": longitude,
        "latitude": latitude
    }
    response = api.search_items(product, location)

    assert response.status_code == 200

    data = response.json()
    header_text = data["header"]["text"]

    assert header_text.startswith("Найден")
    assert "результат" in header_text

@pytest.mark.parametrize("product, longitude, latitude", [
    ("milk",  73.46727297021081, 54.89559112123436),
    ("sushi", 37.617698, 55.755864),
    ("kinder", 30.315868, 59.939095),
])
def test_search_in_english(api, product, longitude, latitude):
    location = {
        "longitude": longitude,
        "latitude": latitude
    }
    response = api.search_items(product, location)

    assert response.status_code == 200

    data = response.json()
    header_text = data["header"]["text"]

    assert header_text.startswith("Найден")
    assert "результат" in header_text


@pytest.mark.parametrize("product, longitude, latitude", [
    ("молоко 3", 73.46727297021081, 54.89559112123436)
])
def test_search_with_numbers(api, product, longitude, latitude):
    location = {
        "longitude": longitude,
        "latitude": latitude
    }
    response = api.search_items(product, location)

    assert response.status_code == 200

    data = response.json()
    header_text = data["header"]["text"]

    assert header_text == "Увы, ничего не найдено"


@pytest.mark.parametrize("product, longitude, latitude", [
    ("молоко 3", 73.46727297021081, 54.89559112123436)
])
def test_search_with_numbers(api, product, longitude, latitude):
    location = {
        "longitude": longitude,
        "latitude": latitude
    }
    response = api.search_items(product, location)

    assert response.status_code == 200

    data = response.json()
    header_text = data["header"]["text"]

    assert header_text == "Ничего не нашли, но есть:"


@pytest.mark.parametrize("product, longitude, latitude", [
    ("екыирыкиртеьнебешгбпбпьбакьбкнбькабабьакгьгбаьбанбакннгьбангбнбанбанбаннабнабнбангьаньаньаньаньаньбанбаабанбнабанбьананннбанбабабан",
     73.46727297021081, 54.89559112123436)
])
def test_search_long_name(api, product, longitude, latitude):
    location = {
        "longitude": longitude,
        "latitude": latitude
    }
    response = api.search_items(product, location)

    assert response.status_code == 200

    data = response.json()
    header_text = data["header"]["text"]

    assert header_text == "Ничего не нашли, но есть:"


@pytest.mark.parametrize("product, longitude, latitude", [
    ("молоко", 73.46727297021081, 54.89559112123436)
])
def test_search_invalid_method(api, product, longitude, latitude):
    location = {
        "longitude": longitude,
        "latitude": latitude
    }
    response = api.search_items_invalid_method(product, location)

    assert response.status_code == 405
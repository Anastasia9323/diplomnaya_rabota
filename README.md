# diplomnaya_rabota

# Дипломная работа 

### Проект - Сервис по доставке еды Деливери - это современный сервис по доставке еды, который позволяет быстро и удобно заказывать блюда из различных ресторанов прямо на дом или в офис. https://market-delivery.yandex.ru
### Ссылка на финалный проект по ручному тестированию  https://klimenkova.yonote.ru/share/af3aff58-e8b8-411a-8294-e7fb2362442e

## Тесты UI:
1. Smoke - Загрузка главной страницы
2. Добавление товара в корзину
2. Увеличение количества товаров в корзине
3. Уменьшениеколичества товаров в корзине
4. Удаление товара из корзины

## Тесты API:
1. Поиск на кириллице 
2. Поиск на латинице
3. Поиск с цифрами 
4. Пустой поиск 
5. Поиск с длинным название 
6. Запрос на поиск с методом PUT вместо POST


### Шаги
1. Склонировать проект `git clone https://github.com/Anastasia9323/diplomnaya_rabota.git`
2. Установить все зависимости `pip3 install > -r requirements.txt`
3. Запустить тесты `pytest`
4. Сгенерировать отчет `allure generate allure-files -o allure-report`
5. Открыть отчет `allure open allure-report`

### Стек:
- pytest
- selenium
- webdriver manager
- requests
- allure


## Структура:
- ./test - тесты
- ./pages - описание страниц
- ./api - описание API


### Полезные ссылки
- [Подсказка по markdown](https://www.markdownguide.org/basic-syntax/)
- [Генератор файла .gitignore](https://www.toptal.com/developers/gitignore)
- [Про pip freeze](https://pip.pypa.io/en/stable/cli/pip_freeze/) 

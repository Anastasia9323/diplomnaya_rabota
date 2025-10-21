# diplomnaya_rabota

## Шаблон для автоматизации тестирования на python


## Тесты UI:
1. Добавление товара в корзину
2. Удаление товара из корзины
3. 





### Шаги
1. Склонировать проект 'git clone "https://github.com/Anastasia9323/diplomnaya_rabota.git"
2. Установить все зависимости 'pip3 install > -r requirements.txt'
3. Запустить тесты 'pytest'
4. Сгенерировать отчет 'allure generate allure-files -o allure-report'
5. Открыть отчет 'allure open allure-report'

### Стек:
- pytest
- selenium
- webdriver manager
- requests
- _sqlalchemy_
- allure
- configuration
- json

## Структура:
- ./test - тесты
- ./pages - описание страниц
- ./api - хелперы для работы с API
- ./db - хелперы для работы с БД (?)
- ./configuration = провайдер настроек
    - test_config.ini - настройка для тестов
- ./testdata - провайдер тестовых данных
    - test_data.json


### Полезные ссылки
- [Подсказка по markdown](https://www.markdownguide.org/basic-syntax/)
- [Генератор файла .gitignore](https://www.toptal.com/developers/gitignore)
- [Про pip freeze](https://pip.pypa.io/en/stable/cli/pip_freeze/) 

### Библиотеки (!)
- pip3 install pytest
- pip3 install selenium
- pip3 install webdriver-manager
- pip3 install allure-pytest
- pip3 install requests
# Проект автоматизированного тестирования autotests_project1

## Описание
Данный проект содержит структуру для автоматизированного тестирования веб-приложений:
- `api_tests/` — тесты для проверки REST API.
- `selenium_tests/` — UI тесты с использованием Selenium WebDriver.
    - `fixtures/` — содержит фикстуры для подготовки данных.
    - `locators/` — содержит локаторы элементов страниц.

## Требования
- Python 3.8+
- Установленный Chrome Browser (для Selenium)

## Установка и запуск
1. Клонируйте репозиторий:
   https://github.com/mooncna/autotests_project1/
   git clone https://github.com/mooncna/autotests_project1/
2. python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python -m pytest            — все тесты
python -m pytest api_tests  — только API
python -m pytest selenium_tests — только UI
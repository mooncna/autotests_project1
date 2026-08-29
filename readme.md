#№ Проект содержит структуру для автоматизированного тестирования веб-приложений:
- `api_tests/` — тесты для проверки REST API.
- `selenium_tests/` — UI-тесты для https://www.saucedemo.com/ с использованием Selenium WebDriver.
    - `locators/` — локаторы элементов страниц (login, inventory, cart, checkout), используются централизованно во всех тестах.
    - `fixtures/` — фикстуры pytest для инициализации WebDriver и авторизации (`driver`, `logged_in_driver`).
    - `tests/` — сами тесты, разложенные по сценариям:
        - `tests/auth` — негативный сценарий авторизации.
        - `tests/cart` — очистка корзины.
        - `tests/purchase` — успешная покупка.
    - `utils/` — вспомогательные функции, переиспользуемые в тестах (работа с корзиной, форма оформления заказа).

## Требования[locators](selenium_tests/locators)
- Python 3.8+
- Установленный Chrome Browser (для Selenium)

## Установка и запуск
1. Клонируйте репозиторий:
   ```
   git clone https://github.com/mooncna/autotests_project1/
   ```
2. Настройте окружение:
   ```
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Запустите тесты:
   ```
   python -m pytest                      # все тесты
   python -m pytest api_tests            # только API
   python -m pytest selenium_tests       # только UI (Selenium)
   python -m pytest -v                  # с подробным выводом
   ```

## Тестовые сценарии Selenium (Практическая работа 8)
1. **Успешная покупка** (`selenium_tests/tests/purchase/test_successful_purchase.py`) — авторизация, добавление товара в корзину, оформление заказа, проверка сообщения об успехе.
2. **Очищение корзины** (`selenium_tests/tests/cart/test_cart_clear.py`) — добавление нескольких товаров, полная очистка корзины, возврат в каталог.
3. **Неуспешная авторизация** (`selenium_tests/tests/auth/test_login_negative.py`) — вход с неверными данными, проверка текста ошибки.

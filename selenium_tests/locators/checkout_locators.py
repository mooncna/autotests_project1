from selenium.webdriver.common.by import By


class CheckoutPageLocators:
    """Локаторы для шагов оформления заказа."""

    # 1. Ввод данных покупателя
    first_name_input = (By.ID, "first-name")
    last_name_input = (By.ID, "last-name")
    postal_code_input = (By.ID, "postal-code")
    continue_button = (By.ID, "continue")

    # 2. Обзор заказа (Кнопка "Finish" для финального подтверждения и завершения покупки)
    finish_button = (By.ID, "finish")

    # 3. Подтверждение заказа
    complete_button = (By.CLASS_NAME, "complete-button") # Возврат в каталог товаров
    back_button = (By.CLASS_NAME, "back-to-products")  # или кнопки возврата (дублирует функцию выше)

from selenium.webdriver.common.by import By


class CheckoutPageLocators:
    """Локаторы для шагов оформления заказа (checkout-step-one/two, checkout-complete)."""

    # 1. Ввод данных покупателя (checkout-step-one)
    first_name_input = (By.ID, "first-name")
    last_name_input = (By.ID, "last-name")
    postal_code_input = (By.ID, "postal-code")
    continue_button = (By.ID, "continue")

    # 2. Обзор заказа (checkout-step-two)
    finish_button = (By.ID, "finish")  # Кнопка "Finish" для финального подтверждения покупки

    # 3. Подтверждение заказа (checkout-complete)
    complete_header = (By.CLASS_NAME, "complete-header")  # Заголовок "Thank you for your order!"
    back_home_button = (By.ID, "back-to-products")  # Кнопка возврата в каталог товаров

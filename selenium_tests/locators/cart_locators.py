from selenium.webdriver.common.by import By


class CartPageLocators:
    """Локаторы для страницы корзины (cart.html)."""

    page_title = (By.CLASS_NAME, "title")  # Заголовок страницы "Your Cart"
    cart_item = (By.CLASS_NAME, "cart_item")  # Карточка товара в корзине
    remove_buttons = (By.CSS_SELECTOR, "button[data-test^='remove-']")  # Кнопки "Remove"
    checkout_button = (By.ID, "checkout")  # Кнопка "Checkout"
    continue_shopping_button = (By.ID, "continue-shopping")  # Кнопка "Continue shopping"

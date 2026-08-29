from selenium.webdriver.common.by import By


class CartPageLocators:
    """Локаторы для страницы корзины (cart.html)."""

    page_title = (By.CLASS_NAME, "title") # Заголовок страницы "Your Cart" (используется для проверки успешного перехода в корзину)
    cart_item = (By.CLASS_NAME, "cart_item") # Карточка товара в корзине (используется для подсчета количества товаров и проверки содержимого корзины)
    remove_button = (By.CSS_SELECTOR, "button[data-test^='remove-']")     # Кнопки "Remove" для удаления товаров.
    checkout_button = (By.ID, "checkout")     # Кнопка "Checkout" для перехода к оформлению заказа (ввод данных покупателя)
    continue_shopping_button = (By.ID, "continue-shopping")     # Кнопка "Continue shopping" для возврата на страницу каталога товаров без оформления заказа


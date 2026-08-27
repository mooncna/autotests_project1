from selenium.webdriver.common.by import By


class CartPageLocators:
    """Локаторы для страницы корзины (cart.html)."""

    PAGE_TITLE = (By.CLASS_NAME, "title")
    CART_ITEM = (By.CLASS_NAME, "cart_item")
    # По той же логике, что и ADD_TO_CART_BUTTONS: data-test у кнопки "Remove"
    # уникален для каждого товара и не пересекается с кнопками "Add to cart".
    REMOVE_BUTTONS = (By.CSS_SELECTOR, "button[data-test^='remove-']")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")

from selenium.webdriver.common.by import By


class InventoryPageLocators:
    """Локаторы для страницы каталога товаров (inventory.html)."""

    PAGE_TITLE = (By.CLASS_NAME, "title")
    INVENTORY_LIST = (By.CLASS_NAME, "inventory_list")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    # data-test у кнопок "Add to cart" меняется на "remove-..." после добавления
    # товара в корзину, поэтому селектор не захватит уже нажатые кнопки.
    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, "button[data-test^='add-to-cart-']")
    CART_LINK = (By.CSS_SELECTOR, "a[data-test='shopping-cart-link']")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

from selenium.webdriver.common.by import By


class InventoryPageLocators:
    """Локаторы для страницы каталога товаров (inventory.html)."""


    page_title = (By.CLASS_NAME, "title")  # Заголовок страницы "Products"
    inventory_list = (By.CLASS_NAME, "inventory_list") # Контейнер со списком всех товаров
    inventory_items = (By.CLASS_NAME, "inventory_item") # Карточки товаров
    add_to_cart_buttons = (By.CSS_SELECTOR, "button[data-test^='add-to-cart-']")   # Кнопки "Add to cart"
    cart_link = (By.CSS_SELECTOR, "a[data-test='shopping-cart-link']")  # Ссылка-иконка корзины в правом верхнем углу (используется для перехода на страницу корзины)
    cart_badge = (By.CLASS_NAME, "shopping_cart_badge") # Cчетчик количества товаров на иконке корзины

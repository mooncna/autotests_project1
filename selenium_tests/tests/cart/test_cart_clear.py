from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenium_tests.locators.cart_locators import CartPageLocators
from selenium_tests.locators.inventory_locators import InventoryPageLocators
from selenium_tests.utils.helpers import (
    clear_cart_before_test,
    get_cart_badge_count,
    open_cart,
    remove_all_items_from_cart,
)


def test_clear_cart(logged_in_driver):
    """Сценарий 2: добавить товары в корзину, полностью очистить её и вернуться в каталог."""
    driver = logged_in_driver
    clear_cart_before_test(driver)

    add_buttons = driver.find_elements(*InventoryPageLocators.add_to_cart_buttons)
    items_to_add = min(3, len(add_buttons))
    for i in range(items_to_add):
        add_buttons[i].click()
        WebDriverWait(driver, 5).until(
            lambda d, expected=i + 1: get_cart_badge_count(d) == expected
        )

    open_cart(driver)
    cart_items = driver.find_elements(*CartPageLocators.cart_item)
    assert len(cart_items) == items_to_add, (
        f"Ожидалось {items_to_add} товаров в корзине, найдено {len(cart_items)}"
    )

    remove_all_items_from_cart(driver)
    driver.find_element(*CartPageLocators.continue_shopping_button).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(InventoryPageLocators.page_title)
    )

    cart_items_after = driver.find_elements(*CartPageLocators.cart_item)
    assert len(cart_items_after) == 0, "Корзина не пуста после очистки"
    assert get_cart_badge_count(driver) == 0, "Значок количества товаров в корзине должен исчезнуть"
    assert "inventory.html" in driver.current_url, "Пользователь не вернулся на страницу товаров"

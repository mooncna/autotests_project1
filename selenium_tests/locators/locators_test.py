from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def demo_login():
    # Запуск драйвера
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    print("\n===== ЛОКАТОРЫ НА SAUCEDEMO =====")

    # 1. По ID — поле username
    username = driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")
    print("✅ По ID: поле username найдено")

    # 2. По ID — поле password
    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")
    print("✅ По ID: поле password найдено")

    # 3. По NAME — атрибут name у поля ввода
    username_by_name = driver.find_element(By.NAME, "user-name")
    print("✅ По NAME: поле username найдено")

    # 4. По TAG_NAME — все input на странице
    inputs = driver.find_elements(By.TAG_NAME, "input")
    print(f"✅ По TAG_NAME: найдено input: {len(inputs)}")

    # 5. По ID — кнопка Login
    login_btn = driver.find_element(By.ID, "login-button")
    print(f"✅ По ID: кнопка '{login_btn.get_attribute('value')}' найдена")

    # 6. По CLASS_NAME — логотип
    logo = driver.find_element(By.CLASS_NAME, "login_logo")
    print(f"✅ По CLASS_NAME: логотип '{logo.text}'")

    # 7. По CSS — блок с тестовыми данными
    credentials = driver.find_element(By.CSS_SELECTOR, "#login_credentials")
    print(f"✅ По CSS: блок с данными найден")

    # Нажимаем кнопку Login
    login_btn.click()
    time.sleep(2)

    # 8. Проверка — заголовок страницы товаров
    title = driver.find_element(By.CLASS_NAME, "title")
    print(f"✅ Заголовок страницы: '{title.text}'")

    # 9. По CLASS_NAME — все товары
    items = driver.find_elements(By.CLASS_NAME, "inventory_item")
    print(f"✅ Найдено товаров: {len(items)}")

    # 10. По CSS — первый товар
    first_item = driver.find_element(By.CSS_SELECTOR, ".inventory_item:first-child")
    name = first_item.find_element(By.CLASS_NAME, "inventory_item_name")
    price = first_item.find_element(By.CLASS_NAME, "inventory_item_price")
    print(f"✅ Первый товар: '{name.text}' — {price.text}")

    # 11. По CLASS_NAME — кнопка Add to cart у первого товара
    add_btn = first_item.find_element(By.CLASS_NAME, "btn_inventory")
    print(f"✅ По CLASS_NAME: кнопка '{add_btn.text}'")

    # 12. По XPath — кнопка у первого товара
    add_btn_xpath = driver.find_element(By.XPATH, "(//div[@class='inventory_item'])[1]//button")
    print(f"✅ По XPath: кнопка '{add_btn_xpath.text}'")

    # 13. По CSS (data-test) — ссылка на корзину
    cart_link = driver.find_element(By.CSS_SELECTOR, "a[data-test='shopping-cart-link']")
    print("✅ По CSS (data-test): корзина найдена")

    # 14. По XPath — карточка товара по тексту
    backpack = driver.find_element(
        By.XPATH, "//div[@data-test='inventory-item-name'][text()='Sauce Labs Backpack']"
    )
    print(f"✅ По XPath (текст): '{backpack.text}'")

    # 15. По ID — кнопка-три точки (открывает меню)
    burger = driver.find_element(By.ID, "react-burger-menu-btn")
    burger.click()
    time.sleep(2)  # ждём открытия меню
    print("✅ По ID: кнопка меню (бургер) найдена")

    # 16. По ID — пункт Logout в меню
    logout_link = driver.find_element(By.ID, "logout_sidebar_link")
    print("✅ По ID: пункт меню 'Logout' найден")

    time.sleep(3)
    driver.quit()

if __name__ == "__main__":
    demo_login()
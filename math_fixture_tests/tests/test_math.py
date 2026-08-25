from operations import add_numbers
from tests.settingstest import math_test_data

def test_addition(math_test_data):
    """
    Тест проверяет корректность сложения любого количества чисел
    с использованием параметризованной фикстуры из conftest.py.
    """
    # Распаковываем данные, полученные из фикстуры
    numbers, expected_result = math_test_data

    # Вызываем функцию сложения, распаковывая кортеж чисел через *
    actual_result = add_numbers(*numbers)

    # Проверяем, что результат совпадает с ожидаемым
    assert actual_result == expected_result, \
        f"Ошибка при сложении {numbers}. Ожидалось {expected_result}, получено {actual_result}"
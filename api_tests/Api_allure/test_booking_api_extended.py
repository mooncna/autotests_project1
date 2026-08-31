import allure
import pytest
import requests


# ------------------------------------------------------------
# 1. GET-ЗАПРОСЫ
# ------------------------------------------------------------

@allure.epic("API Тестирование")
@allure.feature("Бронирования")
@allure.story("GET запросы")
@allure.title("Получение списка всех бронирований")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_all_bookings(base_url):
    """Получение списка всех бронирований"""
    with allure.step("Отправка GET запроса на /booking"):
        response = requests.get(f"{base_url}/booking")

    with allure.step("Проверка статуса ответа"):
        assert response.status_code == 200, f"GET /booking failed with {response.status_code}"

    with allure.step("Проверка структуры ответа"):
        bookings = response.json()
        assert isinstance(bookings, list), "Ответ не является списком"
        assert len(bookings) > 0, "Список бронирований пуст"

    allure.attach(
        f"Количество бронирований: {len(bookings)}",
        name="bookings_count",
        attachment_type=allure.attachment_type.TEXT
    )


@allure.epic("API Тестирование")
@allure.feature("Бронирования")
@allure.story("GET запросы")
@allure.title("Получение конкретного бронирования по ID")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_booking_by_id(base_url, create_booking_id):
    """Получение конкретного бронирования по ID"""
    booking_id = create_booking_id

    with allure.step(f"Отправка GET запроса на /booking/{booking_id}"):
        response = requests.get(f"{base_url}/booking/{booking_id}")

    with allure.step("Проверка статуса ответа"):
        assert response.status_code == 200, f"GET /booking/{booking_id} failed"

    with allure.step("Проверка данных бронирования"):
        booking = response.json()
        assert booking.get("firstname") == "Ivan", "Имя не совпадает"
        assert booking.get("lastname") == "Petrov", "Фамилия не совпадает"
        assert booking.get("totalprice") == 150, "Цена не совпадает"

    allure.attach(
        response.text,
        name="booking_data",
        attachment_type=allure.attachment_type.JSON
    )


@allure.epic("API Тестирование")
@allure.feature("Бронирования")
@allure.story("GET запросы")
@allure.title("Проверка нескольких ID (параметризация)")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("booking_id", [1, 2, 3])
def test_get_multiple_bookings(base_url, booking_id):
    """Параметризованный тест для нескольких ID"""
    with allure.step(f"Отправка GET запроса на /booking/{booking_id}"):
        response = requests.get(f"{base_url}/booking/{booking_id}")

    with allure.step("Проверка статуса ответа"):
        assert response.status_code == 200, f"Booking {booking_id} не найден"

    with allure.step("Проверка наличия поля firstname"):
        assert "firstname" in response.json(), "Нет поля firstname"


@allure.epic("API Тестирование")
@allure.feature("Бронирования")
@allure.story("GET запросы")
@allure.title("Несуществующее бронирование → 404")
@allure.severity(allure.severity_level.NORMAL)
def test_get_nonexistent_booking(base_url):
    """Негативный тест: несуществующее бронирование → 404"""
    with allure.step("Отправка GET запроса на /booking/999999"):
        response = requests.get(f"{base_url}/booking/999999")

    with allure.step("Проверка статуса ответа"):
        assert response.status_code == 404, f"Ожидался 404, получен {response.status_code}"


# ------------------------------------------------------------
# 2. POST-ЗАПРОСЫ (СОЗДАНИЕ)
# ------------------------------------------------------------

@allure.epic("API Тестирование")
@allure.feature("Бронирования")
@allure.story("POST запросы")
@allure.title("Создание бронирования без авторизации")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_booking_without_auth(base_url):
    """Создание бронирования без авторизации (должно работать)"""
    payload = {
        "firstname": "John",
        "lastname": "Doe",
        "totalprice": 200,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2025-02-01",
            "checkout": "2025-02-10"
        },
        "additionalneeds": "Parking"
    }

    with allure.step(f"Отправка POST запроса на /booking с данными: {payload}"):
        response = requests.post(f"{base_url}/booking", json=payload)

    with allure.step("Проверка статуса ответа"):
        assert response.status_code == 200, "Не удалось создать бронирование"

    with allure.step("Проверка структуры ответа"):
        data = response.json()
        assert "bookingid" in data, "Нет ID созданного бронирования"
        assert data["booking"]["firstname"] == "John", "Имя не совпадает"

    allure.attach(
        response.text,
        name="created_booking",
        attachment_type=allure.attachment_type.JSON
    )


# ------------------------------------------------------------
# 3. PUT-ЗАПРОСЫ (ОБНОВЛЕНИЕ)
# ------------------------------------------------------------

@allure.epic("API Тестирование")
@allure.feature("Бронирования")
@allure.story("PUT запросы")
@allure.title("Полное обновление бронирования через PUT")
@allure.severity(allure.severity_level.CRITICAL)
def test_update_booking(auth_headers, create_booking_id, base_url):
    """Обновление существующего бронирования через PUT"""
    booking_id = create_booking_id
    update_payload = {
        "firstname": "Ivan",
        "lastname": "Sidorov",
        "totalprice": 250,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-03-01",
            "checkout": "2025-03-10"
        },
        "additionalneeds": "Breakfast and Wi-Fi"
    }

    with allure.step(f"Отправка PUT запроса на /booking/{booking_id}"):
        response = requests.put(
            f"{base_url}/booking/{booking_id}",
            json=update_payload,
            headers=auth_headers
        )

    with allure.step("Проверка статуса ответа"):
        assert response.status_code == 200, f"PUT failed with {response.status_code}"

    with allure.step("Проверка обновлённых данных"):
        updated = response.json()
        assert updated.get("lastname") == "Sidorov", "Фамилия не обновилась"
        assert updated.get("totalprice") == 250, "Цена не обновилась"

    allure.attach(
        response.text,
        name="updated_booking",
        attachment_type=allure.attachment_type.JSON
    )


# ------------------------------------------------------------
# 4. PATCH-ЗАПРОСЫ (ЧАСТИЧНОЕ ОБНОВЛЕНИЕ)
# ------------------------------------------------------------

@allure.epic("API Тестирование")
@allure.feature("Бронирования")
@allure.story("PATCH запросы")
@allure.title("Частичное обновление бронирования через PATCH")
@allure.severity(allure.severity_level.NORMAL)
def test_patch_booking(auth_headers, create_booking_id, base_url):
    """Частичное обновление через PATCH (меняем только цену)"""
    booking_id = create_booking_id
    patch_payload = {"totalprice": 300}

    with allure.step(f"Отправка PATCH запроса на /booking/{booking_id}"):
        response = requests.patch(
            f"{base_url}/booking/{booking_id}",
            json=patch_payload,
            headers=auth_headers
        )

    with allure.step("Проверка статуса ответа"):
        assert response.status_code == 200, f"PATCH failed with {response.status_code}"

    with allure.step("Проверка обновлённых данных"):
        patched = response.json()
        assert patched.get("totalprice") == 300, "Цена не обновилась"
        assert patched.get("firstname") == "Ivan", "Имя изменилось (а должно остаться)"


# ------------------------------------------------------------
# 5. DELETE-ЗАПРОСЫ (УДАЛЕНИЕ)
# ------------------------------------------------------------

@allure.epic("API Тестирование")
@allure.feature("Бронирования")
@allure.story("DELETE запросы")
@allure.title("Создание и удаление бронирования")
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_booking(auth_headers, base_url):
    """Создаём бронирование и сразу удаляем его"""
    payload = {
        "firstname": "Delete",
        "lastname": "Me",
        "totalprice": 50,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2025-01-01",
            "checkout": "2025-01-02"
        }
    }

    with allure.step("Создание бронирования для удаления"):
        create_resp = requests.post(f"{base_url}/booking", json=payload)
        assert create_resp.status_code == 200, "Не удалось создать бронирование для удаления"
        booking_id = create_resp.json().get("bookingid")

    with allure.step(f"Отправка DELETE запроса на /booking/{booking_id}"):
        delete_resp = requests.delete(
            f"{base_url}/booking/{booking_id}",
            headers=auth_headers
        )

    with allure.step("Проверка статуса ответа"):
        assert delete_resp.status_code in [201, 204], f"DELETE вернул {delete_resp.status_code}"


# ------------------------------------------------------------
# 6. НЕГАТИВНЫЕ ТЕСТЫ (БЕЗ АВТОРИЗАЦИИ)
# ------------------------------------------------------------

@allure.epic("API Тестирование")
@allure.feature("Бронирования")
@allure.story("Негативные тесты")
@allure.title("Обновление без авторизации → 403")
@allure.severity(allure.severity_level.NORMAL)
def test_update_without_auth(create_booking_id, base_url):
    """Обновление без авторизации → 403"""
    booking_id = create_booking_id

    with allure.step(f"Отправка PUT запроса на /booking/{booking_id} без токена"):
        response = requests.put(
            f"{base_url}/booking/{booking_id}",
            json={"firstname": "Hacker"}
        )

    with allure.step("Проверка статуса ответа"):
        assert response.status_code == 403, f"Ожидался 403, получен {response.status_code}"


@allure.epic("API Тестирование")
@allure.feature("Бронирования")
@allure.story("Негативные тесты")
@allure.title("Удаление без авторизации → 403")
@allure.severity(allure.severity_level.NORMAL)
def test_delete_without_auth(create_booking_id, base_url):
    """Удаление без авторизации → 403"""
    booking_id = create_booking_id

    with allure.step(f"Отправка DELETE запроса на /booking/{booking_id} без токена"):
        response = requests.delete(f"{base_url}/booking/{booking_id}")

    with allure.step("Проверка статуса ответа"):
        assert response.status_code == 403, f"Ожидался 403, получен {response.status_code}"


# ============================================================
# ДОПОЛНИТЕЛЬНЫЕ ТЕСТЫ
# ============================================================

# ------------------------------------------------------------
# POST /auth — успешная авторизация 
# ------------------------------------------------------------

@allure.epic("API Тестирование")
@allure.feature("Бронирования")
@allure.story("Авторизация")
@allure.title("Успешная авторизация с верными учётными данными")
@allure.severity(allure.severity_level.CRITICAL)
def test_auth_success(base_url):
   
    payload = {"username": "admin", "password": "password123"}

    with allure.step("Отправка POST запроса на /auth с верными данными"):
        response = requests.post(f"{base_url}/auth", json=payload)

    with allure.step("Проверка статуса ответа"):
        assert response.status_code == 200, "Авторизация не удалась"

    with allure.step("Проверка наличия токена в ответе"):
        body = response.json()
        assert "token" in body, "В ответе нет поля token"
        assert len(body["token"]) > 0, "Токен пустой"

    allure.attach(response.text, name="auth_response", attachment_type=allure.attachment_type.JSON)


# ------------------------------------------------------------
# POST /auth — неверный пароль (негативный тест)
# ------------------------------------------------------------

@allure.epic("API Тестирование")
@allure.feature("Бронирования")
@allure.story("Авторизация")
@allure.title("Авторизация с неверным паролем")
@allure.severity(allure.severity_level.NORMAL)
def test_auth_invalid_credentials(base_url):
    """Важная особенность API: при неверном пароле сервис возвращает
    HTTP 200 (а не 401/403), а в теле ответа — поле "reason" вместо токена."""
    payload = {"username": "admin", "password": "wrong_password"}

    with allure.step("Отправка POST запроса на /auth с неверным паролем"):
        response = requests.post(f"{base_url}/auth", json=payload)

    with allure.step("Проверка статуса ответа"):
        assert response.status_code == 200, f"Неожиданный статус {response.status_code}"

    with allure.step("Проверка тела ответа — токен не выдан, есть причина отказа"):
        body = response.json()
        assert "token" not in body, "Токен не должен выдаваться при неверном пароле"
        assert body.get("reason") == "Bad credentials", "Неверный текст причины отказа"


# ------------------------------------------------------------
# PATCH без авторизации → 403
# ------------------------------------------------------------

@allure.epic("API Тестирование")
@allure.feature("Бронирования")
@allure.story("Негативные тесты")
@allure.title("Частичное обновление без авторизации → 403")
@allure.severity(allure.severity_level.NORMAL)
def test_patch_without_auth(create_booking_id, base_url):
    """У преподавателя без токена проверены PUT и DELETE, но не PATCH —
    закрываем этот пробел."""
    booking_id = create_booking_id

    with allure.step(f"Отправка PATCH запроса на /booking/{booking_id} без токена"):
        response = requests.patch(
            f"{base_url}/booking/{booking_id}",
            json={"totalprice": 1},
        )

    with allure.step("Проверка статуса ответа"):
        assert response.status_code == 403, f"Ожидался 403, получен {response.status_code}"


# ------------------------------------------------------------
# GET /booking/{нечисловой id} → 404
# ------------------------------------------------------------

@allure.epic("API Тестирование")
@allure.feature("Бронирования")
@allure.story("Негативные тесты")
@allure.title("Запрос бронирования с нечисловым ID")
@allure.severity(allure.severity_level.MINOR)
def test_get_booking_non_numeric_id(base_url):
    """есть тест проверяющий несуществующий числовой ID (999999). 
    Здесь првоеряем некорректный формат ID."""
    with allure.step("Отправка GET запроса на /booking/abcdef"):
        response = requests.get(f"{base_url}/booking/abcdef")

    with allure.step("Проверка статуса ответа"):
        assert response.status_code == 404, f"Ожидался 404, получен {response.status_code}"


# ============================================================
# ЗАПУСК
# ============================================================

if __name__ == "__main__":
    pytest.main(["-v", "--tb=short", "--alluredir=allure-results", __file__])

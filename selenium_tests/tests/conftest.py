# Делает фикстуры driver и logged_in_driver из selenium_tests/fixtures/browser_fixture.py
# видимыми для всех тестов в этом пакете (auth/, cart/, purchase/).
# pytest автоматически подхватывает conftest.py во всех вложенных папках —
# отдельная регистрация плагином не нужна.
from selenium_tests.fixtures.browser_fixture import driver, logged_in_driver  # noqa: F401

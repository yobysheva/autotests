import pytest
import allure
from pages.login_page import LoginPage

@allure.feature("Модуль авторизации")
class TestLogin:

    @allure.story("1: Успешный вход")
    @allure.description("Проверка авторизации стандартного пользователя с валидными данными")
    def test_case_1_successful_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")
        assert "/inventory.html" in driver.current_url

    @allure.story("2: Вход заблокированным пользователем")
    @allure.description("Проверка вывода ошибки при попытке входа под locked_out_user")
    def test_case_2_locked_out_user(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("locked_out_user", "secret_sauce")
        error_text = login_page.get_error_message()
        assert "Sorry, this user has been locked out" in error_text

    @allure.story("3: Валидация пустых полей")
    @allure.description("Проверка вывода ошибки, если поля логина и пароля не заполнены")
    def test_case_3_empty_fields_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("", "")
        error_text = login_page.get_error_message()
        assert "Username is required" in error_text
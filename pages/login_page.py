from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

class LoginPage(BasePage):
    USERNAME_INPUT = (By.CSS_SELECTOR, "input#user-name")
    PASSWORD_INPUT = (By.XPATH, "//input[@data-test='password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".submit-button.btn_action")
    ERROR_CONTAINER = (By.XPATH, "//h3[@data-test='error']")

    @allure.step("Авторизация пользователем: '{username}'")
    def login(self, username, password):
        self.find_element(self.USERNAME_INPUT).send_keys(username)
        self.find_element(self.PASSWORD_INPUT).send_keys(password)
        self.click_to(self.LOGIN_BUTTON)

    @allure.step("Получение текста ошибки авторизации")
    def get_error_message(self):
        return self.get_text(self.ERROR_CONTAINER)
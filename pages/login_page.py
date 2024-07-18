import allure

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    @allure.step('Ввод емейла пользователя')
    def insert_user_email(self, email):
        self.insert_text_in_field(LoginPageLocators.FIELD_EMAIL, email)

    @allure.step('Ввод пароля пользователя')
    def insert_user_password(self, password):
        self.insert_text_in_field(LoginPageLocators.FIELD_PASSWORD, password)

    @allure.step('Авторизация пользователя')
    def authorization_user(self):
        self.click_element_with_waiting(LoginPageLocators.BUTTON_LOGIN)

    @allure.step('Проверка отображения окна авторизации')
    def text_from_uthorization(self):
        return self.get_text_from_element(LoginPageLocators.BUTTON_LOGIN)
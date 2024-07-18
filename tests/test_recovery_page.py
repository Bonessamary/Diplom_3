import allure

import data
from data import URLs, Objects
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.recovery_page import RecoveryPage


class TestRecoveryPage:

    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль»')
    @allure.description('Проверка, что на странице есть кнопка "Восстановить"')
    def test_go_to_recovery_page(self, driver):
        main_page = MainPage(driver)
        recovery_page = RecoveryPage(driver)

        main_page.click_personal_account()
        assert recovery_page.go_to_recovery_window() == data.Answers.TEXT_BUTTON_RECOVERY

    @allure.title('Проверка ввода почты и клика по кнопке «Восстановить»')
    @allure.description('Проверка отображения страницы для ввода кода из письма')
    def test_input_email(self, driver):
        main_page = MainPage(driver)
        recovery_page = RecoveryPage(driver)
        login_page = LoginPage(driver)

        main_page.click_personal_account()
        recovery_page.go_to_recovery_window()
        login_page.insert_user_email(Objects.EMAIL_USER)
        recovery_page.click_button_recovery()
        recovery_page.wait_for_reset_password()
        assert driver.current_url == URLs.PAGE_RESET_PASSWORD

    @allure.title("Проверка, клик по кнопке показать/скрыть пароль делает поле активным")
    @allure.description('Проверка, что клик по кнопке показать делает поле активным')
    def test_active_field_password(self, driver):
        main_page = MainPage(driver)
        recovery_page = RecoveryPage(driver)
        login_page = LoginPage(driver)

        main_page.click_personal_account()
        recovery_page.go_to_recovery_window()
        login_page.insert_user_email(Objects.EMAIL_USER)
        recovery_page.click_button_recovery()
        recovery_page.wait_for_reset_password()
        recovery_page.click_button_show_hide()
        element = recovery_page.find_field_password_active()
        assert element.is_displayed()
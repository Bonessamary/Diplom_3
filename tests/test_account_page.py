import allure

import data
from data import URLs
from pages.account_page import AccountPage
from pages.login_page import LoginPage
from pages.main_page import MainPage

class TestAccountPage:

    @allure.title('Проверка клика на кнопку «Личный кабинет»')
    @allure.description('Проверка наличия кнопки "Профиль" на странице «Личный кабинет»')
    def test_click_personal_account(self, log_in_system):
        main_page = MainPage(log_in_system)
        account_page = AccountPage(log_in_system)

        main_page.click_personal_account()
        assert account_page.get_text_profile() == data.Answers.HEADER_PROFILE

    @allure.title('Проверка клика на кнопку «История заказов» из личного кабинета')
    @allure.description('Проверка, что по клику на «История заказов» осуществлен переход на страницу истории заказов')
    def test_click_order_history(self, log_in_system):
        main_page = MainPage(log_in_system)
        account_page = AccountPage(log_in_system)
        main_page.click_personal_account()
        account_page.click_order_history()

        assert log_in_system.current_url == URLs.PAGE_ORDER_HISTORY

    @allure.title('Проверка выхода из аккаунта')
    @allure.description('Проверка, что после клика на «Выход» осуществляется переход в форму авторизации')
    def test_click_exit(self, log_in_system):
        main_page = MainPage(log_in_system)
        account_page = AccountPage(log_in_system)
        login_page = LoginPage(log_in_system)
        main_page.click_personal_account()
        account_page.click_exit()
        assert login_page.text_from_uthorization() == data.Answers.TEXT_BUTTON_LOGIN
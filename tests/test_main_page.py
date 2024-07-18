import time

import allure

import data
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestMainPage:

    @allure.title('Проверка перехода по клику на «Конструктор»')
    @allure.description('Проверка, что по клику на «Конструктор» отобразился заголовок тела конструктора')
    def test_click_constructor(self, driver):
        main_page = MainPage(driver)
        assert main_page.show_header_body_constructor() == data.Answers.HEADER_BODY_CONSTRUCTOR

    @allure.title('Проверка перехода по клику на «Лента заказов»')
    @allure.description('Проверка, что отобразился заголовок ленты заказов')
    def test_orders_feed(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.click_orders_feed()
        assert order_page.find_header_order_feed() == data.Answers.HEADER_ORDER_FEED

    @allure.title('Проверка клика на ингредиент')
    @allure.description('Проверка, что если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_click_ingredients_details(self, driver):
        main_page = MainPage(driver)
        assert main_page.show_ingredients_details().text == data.Answers.HEADER_DETAILS_INGREDIENTS

    @allure.title('Проверка клика по крестику в окне "Детали ингредиента"')
    @allure.description('Проверка, что всплывающее окно закрывается кликом по крестику')
    def test_click_close_ingredients_details(self, driver):
        main_page = MainPage(driver)
        assert main_page.close_details_ingredient()

    @allure.title('Проверка счетчика ингредиента')
    @allure.description('Проверка, что при добавлении ингредиента в заказ счётчик этого ингридиента увеличивается')
    def test_count_ingredients(self, driver):
        main_page = MainPage(driver)
        start_count = main_page.count_ingredients()
        main_page.wait_main_page()
        main_page.drag_and_drop_ingredients_to_burger()
        main_page.wait_main_page()
        end_count = main_page.count_ingredients()
        assert end_count > start_count

    @allure.title('Проверка оформления заказа')
    @allure.description('Проверка, что залогиненный пользователь может оформить заказ')
    def test_authorized_user_arrange_order(self, log_in_system):
        main_page = MainPage(log_in_system)
        main_page.drag_and_drop_ingredients_to_burger()
        assert main_page.arrange_order() == data.Answers.TEXT_ARRANGE_ORDER
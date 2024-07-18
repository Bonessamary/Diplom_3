import allure

import data
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title('Проверка отображения деталей заказа')
    @allure.description('Проверяем, что при клике на заказ, откроется всплывающее окно с деталями')
    def test_visible_details_order(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.click_orders_feed()
        assert order_page.get_text_from_details_order() == data.Answers.HEADER_DETAILS_ORDER

    @allure.title('Проверка отображения заказа пользователя в ленте заказов')
    @allure.description('Проверка, что заказы из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_user_order_visible_from_orders_feed(self, log_in_system):
        main_page = MainPage(log_in_system)
        order_page = OrderPage(log_in_system)
        main_page.drag_and_drop_ingredients_to_burger()
        main_page.arrange_order()
        order_number = f'#0{order_page.get_number_of_created_order()}'
        main_page.click_orders_feed()
        assert order_page.get_text_user_order(order_number)

    @allure.title('Проверка счётчика «Выполнено за всё время»')
    @allure.description('Проверка, что при создании нового заказа счётчик «Выполнено за всё время» увеличивается')
    def test_count_all_time_increase(self, log_in_system):
        main_page = MainPage(log_in_system)
        order_page = OrderPage(log_in_system)
        main_page.click_orders_feed()
        start_count_all_time = order_page.get_text_count_all_time()
        main_page.return_main_page()
        main_page.drag_and_drop_ingredients_to_burger()
        main_page.arrange_order()
        order_page.get_number_of_created_order()
        main_page.click_orders_feed()
        end_count_all_time = order_page.get_text_count_all_time()
        assert end_count_all_time > start_count_all_time

    @allure.title('Проверка счётчика «Выполнено за сегодня»')
    @allure.description('Проверка, что при создании нового заказа счётчик «Выполнено за сегодня» увеличивается')
    def test_count_today_increase(self, log_in_system):
        main_page = MainPage(log_in_system)
        order_page = OrderPage(log_in_system)
        main_page.click_orders_feed()
        start_count_today = order_page.get_text_count_today()
        main_page.return_main_page()
        main_page.drag_and_drop_ingredients_to_burger()
        main_page.arrange_order()
        order_page.get_number_of_created_order()
        main_page.click_orders_feed()
        end_count_today = order_page.get_text_count_today()
        assert end_count_today > start_count_today

    @allure.title('Проверка появления заказа в разделе «В работе»')
    @allure.description('Проверка, что после оформления заказа номер заказа появляется в разделе «В работе»')
    def test_appear_order_in_work(self, log_in_system):
        main_page = MainPage(log_in_system)
        order_page = OrderPage(log_in_system)
        main_page.drag_and_drop_ingredients_to_burger()
        main_page.arrange_order()
        order_count = order_page.get_number_of_created_order()
        main_page.click_orders_feed()
        assert order_page.get_text_order_in_work(order_count)
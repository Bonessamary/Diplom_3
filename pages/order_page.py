import allure

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step('Поиск заголовка ленты заказов')
    def find_header_order_feed(self):
        return self.find_element_with_waiting(OrderPageLocators.HEADER_ORDERS_FEED).text

    @allure.step('Текст из формы с деталями заказа')
    def get_text_from_details_order(self):
        self.click_on_element(OrderPageLocators.FIRST_ORDER_IN_LIST)
        return self.get_text_from_element(OrderPageLocators.WINDOW_ORDER_DETAILS)

    @allure.step('Получение номера нового заказа')
    def get_number_of_created_order(self):
        self.wait_change_text_element(OrderPageLocators.WINDOW_CREATED_ORDER, '9999')
        order_number = self.get_text_from_element(OrderPageLocators.WINDOW_CREATED_ORDER)
        self.click_on_element(OrderPageLocators.BUTTON_CLOSE_WINDOW_CREATED_ORDER)
        return order_number

    @allure.step('Поиск заказа по номеру из раздела «История заказов»')
    def get_text_user_order(self, order_number):
        order_in_list_formatted = self.format_locator(OrderPageLocators.CREATED_ORDER_IN_LIST, order_number)
        return self.get_text_from_element(order_in_list_formatted)

    @allure.step('Получение цифры из счётчика «Выполнено за всё время»')
    def get_text_count_all_time(self):
        count_all_time = self.get_text_from_element(OrderPageLocators.COUNT_ALL_TIME)
        return count_all_time

    @allure.step('Получение цифры из счётчика «Выполнено за сегодня»')
    def get_text_count_today(self):
        today_count = self.get_text_from_element(OrderPageLocators.COUNT_TODAY)
        return today_count

    @allure.step('Наличие заказа в разделе «В работе»')
    def get_text_order_in_work(self, order_count):
        order_number_in_work_formatted = self.format_locator(OrderPageLocators.NUMBER_ORDER_IN_WORK, order_count)
        return self.get_text_from_element(order_number_in_work_formatted)
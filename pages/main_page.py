import allure

import locators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Отображение заголовка тела конструктора')
    def show_header_body_constructor(self):
        self.click_element_with_waiting(MainPageLocators.BUTTON_PERSONAL_ACCOUNT)
        self.click_element_with_waiting(MainPageLocators.BUTTON_CONSTRUCTOR)
        return self.find_element_with_waiting(MainPageLocators.HEADER_CONSTRUCTOR).text

    @allure.step('Клик на кнопку "Лента заказов"')
    def click_orders_feed(self):
        self.click_element_with_waiting(MainPageLocators.BUTTON_ORDERS_FEED)

    @allure.step('Клик по кнопке "Личный кабинет')
    def click_personal_account(self):
        self.click_element_with_waiting(locators.main_page_locators.MainPageLocators.BUTTON_PERSONAL_ACCOUNT)

    @allure.step('Клик на ингредиент и поиск заголовка "Детали ингредиента"')
    def show_ingredients_details(self):
        self.click_element_with_waiting(MainPageLocators.OBJECT_INGREDIENT)
        return self.find_element_with_waiting(MainPageLocators.HEADER_DETAILS_INGREDIENT)

    @allure.step('Закрыть детали по ингредиенту')
    def close_details_ingredient(self):
        self.show_ingredients_details()
        self.click_element_with_waiting(MainPageLocators.BUTTON_CLOSE)
        return self.find_element_with_waiting(MainPageLocators.HEADER_CONSTRUCTOR)

    @allure.step('Перетаскивание ингредиентов для бургера')
    def drag_and_drop_ingredients_to_burger(self):
        self.drag_and_drop_ingredient(MainPageLocators.OBJECT_INGREDIENT, MainPageLocators.PLACE_INGREDIENT)

    @allure.step('Счетчик ингредиента')
    def count_ingredients(self):
        return self.get_text_from_element(MainPageLocators.INGREDIENT_COUNT)

    @allure.step('Оформление заказа')
    def arrange_order(self):
        self.click_element_with_waiting(MainPageLocators.BUTTON_ARRANGE_ORDER)
        return self.get_text_from_element(MainPageLocators.CONFIRM_ARRANGE_ORDER)

    @allure.step('Ожидание загрузки главной страницы')
    def wait_main_page(self):
        self.find_element_with_waiting(locators.main_page_locators.MainPageLocators.FORM_MAIN_PAGE)

    @allure.step('Возврат на главную страницу через кнопку с логотипом')
    def return_main_page(self):
        self.click_on_element(MainPageLocators.BUTTON_LOGO)
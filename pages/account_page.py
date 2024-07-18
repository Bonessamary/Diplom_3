import allure
from locators.account_page_locators import AccountPageLocators
from pages.base_page import BasePage


class AccountPage(BasePage):
    @allure.step('Получить текст элемента кнопка "Профиль" в личном кабинете')
    def get_text_profile(self):
        return self.get_text_from_element(AccountPageLocators.BUTTON_PERSONAL_ACCOUNT)

    @allure.step('Клик на кнопку "История заказов"')
    def click_order_history(self):
        self.click_element_with_waiting(AccountPageLocators.BUTTON_ORDER_HISTORY)

    @allure.step('Клик на кнопку "Выход" из аккаунта')
    def click_exit(self):
        self.click_element_with_waiting(AccountPageLocators.BUTTON_EXIT)
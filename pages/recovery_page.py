import allure
import locators
from locators.recovery_page_locators import RecoveryPageLocators
from pages.base_page import BasePage

class RecoveryPage(BasePage):

    @allure.step('Переход в окно восстановления пароля')
    def go_to_recovery_window(self):
        self.click_element_with_waiting(RecoveryPageLocators.LINK_RECOVERY_PASSWORD)
        return self.get_text_from_element(RecoveryPageLocators.BUTTON_RECOVERY)

    @allure.step('Клик по кнопке "Восстановить"')
    def click_button_recovery(self):
        self.click_element_with_waiting(RecoveryPageLocators.BUTTON_RECOVERY)

    @allure.step('Ожидание загрузки страницы reset-password')
    def wait_for_reset_password(self):
        self.find_element_with_waiting(locators.recovery_page_locators.RecoveryPageLocators.FIELD_ENTER_CODE)

    @allure.step('Клик по кнопке показать')
    def click_button_show_hide(self):
        self.click_element_with_waiting(RecoveryPageLocators.BUTTON_SHOW_HIDE)

    @allure.step('Найти подсветку для поля "Пароль"')
    def find_field_password_active(self):
        return self.find_element_with_waiting(RecoveryPageLocators.FIELD_PASSWORD_ACTIVE)
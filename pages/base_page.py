import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Клик по элементу')
    def click_on_element(self, locator):
        element = self.find_element_to_be_clickable(locator)
        self.driver.execute_script("arguments[0].click();", element)
        element = self.find_element_to_be_clickable(locator)
        ActionChains(self.driver).move_to_element(element).click(element).perform()

    @allure.step('Клик по элементу с ожиданием')
    def click_element_with_waiting(self, locator):
        element = self.find_element_with_waiting(locator)
        self.find_element_to_be_clickable(locator)
        element.click()

    @allure.step('Поиск элемента с ожиданием')
    def find_element_with_waiting(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Поиск элемента, пока не станет кликабельным')
    def find_element_to_be_clickable(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    @allure.step('Получение текста из элемента')
    def get_text_from_element(self, locator):
        element = self.find_element_with_waiting(locator)
        return element.text

    @allure.step('Форматирование элемента')
    def format_locator(self, locator, num):
        method, locator_final = locator
        locator_final = locator_final.format(num)
        return method, locator_final

    @allure.step('Заполнение элемента текстом')
    def insert_text_in_field(self, locator, value):
        element = self.find_element_to_be_clickable(locator)
        element.send_keys(value)

    @allure.step('Перетаскивание ингридиента')
    def drag_and_drop_ingredient(self, locator1, locator2):
        object1 = self.find_element_to_be_clickable(locator1)
        object2 = self.find_element_to_be_clickable(locator2)
        action = ActionChains(self.driver)
        action.drag_and_drop(object1, object2).perform()

    @allure.step('Ожидание изменения текста в элементе')
    def wait_change_text_element(self, locator, text_to_be_changed):
        WebDriverWait(self.driver, 10).until_not(expected_conditions.text_to_be_present_in_element(
            locator, text_to_be_changed))
        return self.driver.find_element(*locator)
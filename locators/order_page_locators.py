from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Заголовок ленты заказов
    HEADER_ORDERS_FEED = By.XPATH, "//h1[contains(text(),'Лента заказов')]"

    # Первый заказ в списке
    FIRST_ORDER_IN_LIST = By.XPATH, "/descendant::div[@class='OrderHistory_textBox__3lgbs mb-6'][position() = (1)]"

    # Окно деталей заказу
    WINDOW_ORDER_DETAILS = By.XPATH, "//p[@class='text text_type_main-medium mb-8']"

    # Счетчик выполненных заказов за все время
    COUNT_ALL_TIME = (By.XPATH,
                      "/descendant::p[@class='OrderFeed_number__2MbrQ text text_type_digits-large'][position() = (1)]")

    # Окно созданного заказа
    WINDOW_CREATED_ORDER = (By.XPATH,
                            "//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']")

    # Кнопка закрытия окна созданного заказа
    BUTTON_CLOSE_WINDOW_CREATED_ORDER = (
        By.XPATH,"//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")

    #Созданный заказ в списке заказов
    CREATED_ORDER_IN_LIST = By.XPATH, ".//p[@class = 'text text_type_digits-default' and text()='{}']"

    # Счетчик выполненных заказов за сегодня
    COUNT_TODAY = (By.XPATH, "/descendant::p[@class='OrderFeed_number__2MbrQ text text_type_digits-large'][position() = (2)]")

    # Номера заказов в работе
    NUMBER_ORDER_IN_WORK = By.XPATH, ".//li[@class = 'text text_type_digits-default mb-2' and text()='{}']"
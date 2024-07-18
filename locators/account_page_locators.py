from selenium.webdriver.common.by import By


class AccountPageLocators:
    # Кнопка "Профиль"
    BUTTON_PERSONAL_ACCOUNT = By.XPATH, "//a[contains(text(),'Профиль')]"

    # Кнопка "История заказов"
    BUTTON_ORDER_HISTORY = By.XPATH, '//*[@href="/account/order-history"]'

    # Кнопка "Выход" из профиля
    BUTTON_EXIT = By.XPATH, "//button[contains(text(),'Выход')]"
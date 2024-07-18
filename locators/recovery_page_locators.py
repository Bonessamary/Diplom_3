from selenium.webdriver.common.by import By


class RecoveryPageLocators:
    # Ссылка "Восстановление пароля"
    LINK_RECOVERY_PASSWORD = By.LINK_TEXT, "Восстановить пароль"

    # Кнопка "Восстановить"
    BUTTON_RECOVERY = By.XPATH, "//button[contains(text(),'Восстановить')]"

    # Поле "Введите код из письма"
    FIELD_ENTER_CODE = By.XPATH, "//label[contains(text(),'Введите код из письма')]"

    # Кнопка показать/скрыть пароль
    BUTTON_SHOW_HIDE = By.XPATH, "//div[@class='input__icon input__icon-action']"

    # Подсветка/активность поля пароль
    FIELD_PASSWORD_ACTIVE = By.XPATH, ".//div[@class='input pr-6 pl-6 input_type_text input_size_default input_status_active']"
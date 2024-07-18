from selenium.webdriver.common.by import By


class LoginPageLocators:
    # Кнопка "Войти"
    BUTTON_LOGIN = By.XPATH, "//button[contains(text(),'Войти')]"

    # Поле для ввода Почты в окне регистрации
    FIELD_EMAIL = By.XPATH, ".//label[text()='Email']/following-sibling::input[@type='text']"

    # Поле для ввода Пароля в окне регистрации
    FIELD_PASSWORD = By.XPATH, ".//label[text()='Пароль']/following-sibling::input[@type='password']"
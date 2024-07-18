class URLs:
    MAIN_PAGE = 'https://stellarburgers.nomoreparties.site'
    CREATE_USER = f'{MAIN_PAGE}/api/auth/register'
    INFO_USER = f'{MAIN_PAGE}/api/auth/user'
    PAGE_LOGIN = f'{MAIN_PAGE}/api/auth/login'
    PAGE_RESET_PASSWORD = f'{MAIN_PAGE}/reset-password'
    PAGE_ORDER_HISTORY = f'{MAIN_PAGE}/account/order-history'

class Objects:
    EMAIL_USER = 'but6@yandex.ru'
    BURGER_INGREDIENT = 'Флюоресцентная булка R2-D3'

class Answers:
    HEADER_BODY_CONSTRUCTOR = 'Соберите бургер'
    HEADER_ORDER_FEED = 'Лента заказов'
    HEADER_DETAILS_INGREDIENTS = 'Детали ингредиента'
    TEXT_ARRANGE_ORDER = 'Ваш заказ начали готовить'
    HEADER_DETAILS_ORDER = 'Cостав'
    HEADER_PROFILE = 'Профиль'
    TEXT_BUTTON_LOGIN = 'Войти'
    TEXT_BUTTON_RECOVERY = 'Восстановить'
Задание 3: веб-приложение. 
Тестирование веб-приложения Stellar Burgers, с помощью паттерна Page Object Model. 
Тестирование функциональности проводится в Google Chrome и Mozilla Firefox. 
Подключен Allure-отчёт.

1.test_recovery_page.py - Восстановление пароля
    test_go_to_recovery_page - переход на страницу восстановления пароля по кнопке «Восстановить пароль»,
    test_input_email - ввод почты и клик по кнопке «Восстановить»,
    test_active_field_password - клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.
2.test_account_page.py - Личный кабинет 
    test_click_personal_account - переход по клику на «Личный кабинет»,
    test_click_order_history - переход в раздел «История заказов»,
    test_click_exit - выход из аккаунта.
3.test_main_page.py - Проверка основного функционала
    test_click_constructor - переход по клику на «Конструктор»,
    test_orders_feed - переход по клику на «Лента заказов»,
    test_click_ingredients_details - если кликнуть на ингредиент, появится всплывающее окно с деталями,
    test_click_close_ingredients_details - всплывающее окно закрывается кликом по крестику,
    test_count_ingredients - при добавлении ингредиента в заказ счётчик этого ингридиента увеличивается,
    test_authorized_user_arrange_order - залогиненный пользователь может оформить заказ.
4.test_order_page.py - Раздел «Лента заказов»
    test_visible_details_order - если кликнуть на заказ, откроется всплывающее окно с деталями,
    test_user_order_visible_from_orders_feed - заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»,
    test_count_all_time_increase - при создании нового заказа счётчик Выполнено за всё время увеличивается,
    test_count_today_increase - при создании нового заказа счётчик Выполнено за сегодня увеличивается,
    test_appear_order_in_work - после оформления заказа его номер появляется в разделе В работе.
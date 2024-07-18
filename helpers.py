import allure
import random
import string


def generate_random_string(length):
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


@allure.step('Генерация логина, пароля, имени')
def generate_data_user():
    email = f'{generate_random_string(10)}@yandex.ru'
    password = generate_random_string(10)
    name = generate_random_string(10)
    return email, password, name


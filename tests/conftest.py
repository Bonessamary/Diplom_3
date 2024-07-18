import requests
import pytest
from selenium import webdriver
from helpers import generate_data_user
from data import URLs
from pages.main_page import MainPage
from pages.login_page import LoginPage

@pytest.fixture(scope='function', params=['chrome', 'firefox'])
def driver(request):
    if 'chrome' in request.param:
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)

    elif 'firefox' in request.param:
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=options)

    else:
        raise TypeError("Driver is not found")

    driver.get(URLs.MAIN_PAGE)
    yield driver
    driver.quit()

@pytest.fixture
def register_and_delete_user_api():
    list_data = generate_data_user()

    payload = {
        'email': list_data[0],
        'password': list_data[1],
        'name': list_data[2]
    }
    registration_response = requests.post(URLs.CREATE_USER, data=payload)
    registration_info = []
    if registration_response.status_code == 200:
        registration_info.append(list_data[0])
        registration_info.append(list_data[1])
        registration_info.append(list_data[2])

    yield registration_info

    payload = {
        'email': list_data[0],
        'password': list_data[1]
    }
    login_response = requests.post(URLs.PAGE_LOGIN, data=payload)
    token = login_response.json()['accessToken']
    requests.delete(f'{URLs.INFO_USER}', headers={
        "Authorization": token
    })

@pytest.fixture
def log_in_system(driver, register_and_delete_user_api):
    email = register_and_delete_user_api[0]
    password = register_and_delete_user_api[1]

    main_page = MainPage(driver)
    login_page = LoginPage(driver)

    main_page.click_personal_account()
    login_page.insert_user_email(email)
    login_page.insert_user_password(password)
    login_page.authorization_user()
    main_page.wait_main_page()
    return driver
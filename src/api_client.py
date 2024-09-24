import allure
import requests

from utils import urls as url


@allure.step("Регистрация нового пользователя")
def register_user(data):
    return requests.post(url.REGISTER_URL, json=data)


@allure.step("Аутентификация пользователя")
def auth_user(data):
    return requests.post(url.AUTH_URL, json=data)


@allure.step("Создание заказа с данными и токеном")
def create_order(payload, token):
    headers = {
        "Authorization": token
    }
    return requests.post(url.ORDERS, json=payload, headers=headers)


@allure.step("Получение данных заказа заказа")
def get_order(token):
    headers = {
        "Authorization": token
    }
    return requests.get(url.ORDERS, headers=headers)


@allure.step("Изменение данных пользователя")
def change_user_data(token, data):
    headers = {
        "Authorization": token
    }
    return requests.patch(url.USER_INFO, headers=headers, json=data)

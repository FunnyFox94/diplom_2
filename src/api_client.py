import requests

from utils import urls as url


def register_user(data):
    return requests.post(url.REGISTER_URL, json=data)


def auth_user(data):
    return requests.post(url.AUTH_URL, json=data)


def create_order(payload, token):
    headers = {
        "Authorization": token
    }
    return requests.post(url.ORDERS, json=payload, headers=headers)


def get_order(token):
    headers = {
        "Authorization": token
    }
    return requests.get(url.ORDERS, headers=headers)


def change_user_data(token, data):
    headers = {
        "Authorization": token
    }
    return requests.patch(url.USER_INFO, headers=headers, json=data)

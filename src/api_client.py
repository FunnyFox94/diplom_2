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
    print(type(headers))
    return requests.post(url.CREATE_ORDER, json=payload, headers=headers)

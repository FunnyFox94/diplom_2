import requests

from utils import urls as url


def register_user(data):
    return requests.post(url.REGISTER_URL, json=data)


def auth_user(data):
    return requests.post(url.AUTH_URL, json=data)

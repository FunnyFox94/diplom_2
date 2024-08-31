import random
import string

import requests

from utils import urls


def generate_random_string(length):  # генерирую рандомную строку
    letters = string.ascii_lowercase
    random_string = "".join(random.choice(letters) for _ in range(length))
    return random_string


def generate_register_payload(valid_data=True, has_email=True, has_password=True,
                              has_name=True):  # генерация data для регистрации
    payload = {
        "email": f"{generate_random_string(7)}@gmail.com",
        "password": generate_random_string(10),
        "name": generate_random_string(7)
    }
    if not valid_data:
        payload["email"] = "invalid_data"

    if not has_email:
        payload["email"] = ""

    if not has_password:
        payload["password"] = ""

    if not has_name:
        payload["name"] = ""

    return payload


def generate_creds_for_auth(bad_password=False, bad_email=False, missing_password=False,
                            missing_email=False):  # получаем data для авторизации
    payload = generate_register_payload()

    response = requests.post(urls.REGISTER_URL, json=payload)
    # access_token = response.json()["accessToken"]
    if response.status_code == 200:
        payload = {
            "email": payload["email"],
            "password": payload["password"]
        }

    if bad_password:
        payload["password"] = "123456"

    if bad_email:
        payload["email"] = "momo@gmail.com"

    if missing_password:
        payload["password"] = ""

    if missing_email:
        payload["email"] = ""

    return payload

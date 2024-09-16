import pytest
import requests

import utils.generators as generate
from utils import urls


@pytest.fixture
def get_access_token():
    payload = generate.generate_register_payload()
    response = requests.post(urls.REGISTER_URL, data=payload)
    token = response.json()["accessToken"]
    return token


@pytest.fixture
def get_ingredients():
    return generate.get_ids_form_ingredients_list()


@pytest.fixture
def empty_ingredients_list():
    empty_dict = {
        "ingredients": []
    }
    return empty_dict


@pytest.fixture
def wrong_ingredient_hash():
    wrong_hash = {
        "ingredients": ["awdawd"]
    }
    return wrong_hash


@pytest.fixture
def new_user_data():
    new_user_data = {
        "success": False,
        "user": {
            "email": "momo@gmail.com",
            "name": "123123123"
        }
    }
    return new_user_data

import pytest
import requests

import utils.generators as generate
from utils import urls


@pytest.fixture
def register_data():
    return generate.generate_register_payload()


@pytest.fixture
def auth_data():
    return generate.generate_creds_for_auth()


@pytest.fixture
def get_access_token():
    payload = generate.generate_register_payload()
    response = requests.post(urls.REGISTER_URL, data=payload)
    token = response.json()["accessToken"]
    return token


@pytest.fixture
def empty_auth_token():
    return ""


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

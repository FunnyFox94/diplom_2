import pytest
import utils.generators as generate


@pytest.fixture
def register_data():
    return generate.generate_register_payload()


@pytest.fixture
def auth_data():
    return generate.generate_creds_for_auth()

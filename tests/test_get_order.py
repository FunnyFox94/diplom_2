import src.api_client as api
import utils.text_literals as text


class TestGetOrder:

    def test_get_order_by_auth_user(self, get_ingredients, get_access_token):
        api.create_order(get_ingredients, get_access_token)
        response = api.get_order(get_access_token)
        assert response.status_code == 200

    def test_get_order_by_unauth_user(self, get_ingredients, empty_auth_token, get_access_token):
        response = api.get_order(empty_auth_token)
        assert response.status_code == 401
        assert response.text == text.NOT_AUTHORIZED

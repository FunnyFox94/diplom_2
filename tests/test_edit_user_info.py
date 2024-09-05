import src.api_client as api
import utils.text_literals as text


class TestEditUserInfo:
    def test_edit_user_info_success(self, get_access_token, new_user_data):
        response = api.change_user_data(get_access_token, new_user_data)
        assert response.status_code == 200
        assert response.text == new_user_data

    def test_edit_user_info_with_no_auth(self, empty_auth_token, new_user_data):
        response = api.change_user_data(empty_auth_token, new_user_data)
        assert response.status_code == 401
        assert response.text == text.NOT_AUTHORIZED

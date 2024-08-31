import src.api_client as api
import utils.text_literals as text
import utils.generators as generate


class TestUserAuth:

    def test_user_auth_success(self, auth_data):
        response = api.auth_user(auth_data)
        assert response.status_code == 200

    def test_user_auth_bad_password(self):
        response = api.auth_user(generate.generate_creds_for_auth(bad_password=True))
        assert response.status_code == 401
        assert response.json() == text.BAD_CREDENTIALS

    def test_user_auth_bad_email(self):
        response = api.auth_user(generate.generate_creds_for_auth(bad_email=True))
        assert response.status_code == 401
        assert response.json() == text.BAD_CREDENTIALS

    def test_user_auth_missing_password(self):
        response = api.auth_user(generate.generate_creds_for_auth(missing_password=True))
        assert response.status_code == 401
        assert response.json() == text.BAD_CREDENTIALS

    def test_user_auth_missing_email(self):
        response = api.auth_user(generate.generate_creds_for_auth(missing_email=True))
        assert response.status_code == 401
        assert response.json() == text.BAD_CREDENTIALS

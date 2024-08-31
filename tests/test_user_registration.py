import src.api_client as api
import utils.text_literals as text
import utils.generators as generate


class TestUserRegistration:

    def test_user_registration_success(self, register_data):
        response = api.register_user(register_data)
        assert response.status_code == 200

    def test_user_registration_invalid_data(self):
        response = api.register_user(generate.generate_register_payload(valid_data=False))
        assert response.status_code == 500

    def test_user_registration_already_registered_email(self, register_data):
        response = api.register_user(register_data)
        duplicate_response = api.register_user(register_data)
        assert duplicate_response.status_code == 403
        assert duplicate_response.json() == text.ALREADY_EXIST_USER

    def test_user_registration_missing_email(self):
        response = api.register_user(generate.generate_register_payload(has_email=False))
        assert response.status_code == 403
        assert response.json() == text.MISSING_FIELD

    def test_user_registration_missing_password(self):
        response = api.register_user(generate.generate_register_payload(has_password=False))
        assert response.status_code == 403
        assert response.json() == text.MISSING_FIELD

    def test_user_registration_missing_name(self):
        response = api.register_user(generate.generate_register_payload(has_name=False))
        assert response.status_code == 403
        assert response.json() == text.MISSING_FIELD

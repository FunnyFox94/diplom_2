import allure

import src.api_client as api
import utils.text_literals as text
import utils.generators as generate


@allure.epic('Регистрация пользователя')
@allure.feature('Регистрация через API')
class TestUserRegistration:

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Тест на успешную регистрацию пользователя')
    def test_user_registration_success(self):
        register_data = generate.generate_register_payload()
        response = api.register_user(register_data)
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Тест на регистрацию с некорректными данными')
    def test_user_registration_invalid_data(self):
        response = api.register_user(generate.generate_register_payload(valid_data=False))
        assert response.status_code == 500
        assert text.SERVER_ERROR in response.text

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Тест на регистрацию с уже существующим email')
    def test_user_registration_already_registered_email(self):
        register_data = generate.generate_register_payload()
        api.register_user(register_data)
        duplicate_response = api.register_user(register_data)
        assert duplicate_response.status_code == 403
        assert duplicate_response.json() == text.ALREADY_EXIST_USER

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Тест на регистрацию с отсутствующим email')
    def test_user_registration_missing_email(self):
        response = api.register_user(generate.generate_register_payload(has_email=False))
        assert response.status_code == 403
        assert response.json() == text.MISSING_FIELD

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Тест на регистрацию с отсутствующим паролем')
    def test_user_registration_missing_password(self):
        response = api.register_user(generate.generate_register_payload(has_password=False))
        assert response.status_code == 403
        assert response.json() == text.MISSING_FIELD

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Тест на регистрацию с отсутствующим именем')
    def test_user_registration_missing_name(self):
        response = api.register_user(generate.generate_register_payload(has_name=False))
        assert response.status_code == 403
        assert response.json() == text.MISSING_FIELD

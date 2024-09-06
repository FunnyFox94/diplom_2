import allure

import src.api_client as api
import utils.text_literals as text
import utils.generators as generate


@allure.epic('Авторизация пользователя')
@allure.feature('Авторизация через API')
class TestUserAuth:

    @allure.story('Успешная авторизация')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Тест на успешную авторизацию')
    def test_user_auth_success(self, auth_data):
        response = api.auth_user(auth_data)
        assert response.status_code == 200

    @allure.story('Авторизация с неправильным паролем')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Тест на авторизацию с некорректным паролем')
    def test_user_auth_bad_password(self):
        response = api.auth_user(generate.generate_creds_for_auth(bad_password=True))
        assert response.status_code == 401
        assert response.json() == text.BAD_CREDENTIALS

    @allure.story('Авторизация с неправильным email')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Тест на авторизацию с некорректным email')
    def test_user_auth_bad_email(self):
        response = api.auth_user(generate.generate_creds_for_auth(bad_email=True))
        assert response.status_code == 401
        assert response.json() == text.BAD_CREDENTIALS

    @allure.story('Авторизация с отсутствующим паролем')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Тест на авторизацию с отсутствующим паролем')
    def test_user_auth_missing_password(self):
        response = api.auth_user(generate.generate_creds_for_auth(missing_password=True))
        assert response.status_code == 401
        assert response.json() == text.BAD_CREDENTIALS

    @allure.story('Авторизация с отсутствующим email')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Тест на авторизацию с отсутствующим email')
    def test_user_auth_missing_email(self):
        response = api.auth_user(generate.generate_creds_for_auth(missing_email=True))
        assert response.status_code == 401
        assert response.json() == text.BAD_CREDENTIALS

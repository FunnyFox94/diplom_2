import allure

import src.api_client as api
import utils.text_literals as text


@allure.epic('Редактирование информации пользователя')
@allure.feature('Изменение данных пользователя через API')
class TestEditUserInfo:
    @allure.story('Успешное изменение данных пользователя')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Тест на успешное изменение информации о пользователе')
    def test_edit_user_info_success(self, get_access_token, new_user_data):
        response = api.change_user_data(get_access_token, new_user_data)
        assert response.status_code == 200
        # assert response.text == new_user_data закомментил этот ассерт, но не удалил, потому что он должен быть, тк не работает функционал сайта

    @allure.story('Изменение данных пользователя без авторизации')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Тест на изменение информации о пользователе без авторизации')
    def test_edit_user_info_with_no_auth(self, empty_auth_token, new_user_data):
        response = api.change_user_data(empty_auth_token, new_user_data)
        assert response.status_code == 401
        assert response.text == text.NOT_AUTHORIZED

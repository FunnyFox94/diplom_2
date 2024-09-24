import allure

import src.api_client as api
import utils.text_literals as text
import utils.generators as generate


@allure.epic('Получение информации о заказах')
@allure.feature('Получение заказа через API')
class TestGetOrder:

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Тест на получение заказа авторизованным пользователем')
    def test_get_order_by_auth_user(self, get_access_token):
        get_ingredients = generate.get_ids_form_ingredients_list()
        api.create_order(get_ingredients, get_access_token)
        response = api.get_order(get_access_token)
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Тест на получение заказа неавторизованным пользователем')
    def test_get_order_by_unauth_user(self):
        empty_auth_token = ""
        response = api.get_order(empty_auth_token)
        assert response.status_code == 401
        assert response.text == text.NOT_AUTHORIZED

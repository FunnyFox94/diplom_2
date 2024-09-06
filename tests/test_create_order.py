import allure

import src.api_client as api
import utils.text_literals as text

@allure.epic('Создание заказа')
@allure.feature('Создание заказа через API')
class TestCreateOrder:
    @allure.story('Успешное создание заказа')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Тест на успешное создание заказа')
    def test_create_success_order(self, get_access_token, get_ingredients):
        response = api.create_order(get_ingredients, get_access_token)
        assert response.status_code == 200

    @allure.story('Создание заказа без ингредиентов')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Тест на создание заказа без ингредиентов')
    def test_create_order_without_ingredients(self, get_access_token, empty_ingredients_list):
        response = api.create_order(empty_ingredients_list, get_access_token)
        assert response.text == text.EMPTY_INGREDIENT_LIST
        assert response.status_code == 400

    @allure.story('Создание заказа с некорректным хэшем ингредиента')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Тест на создание заказа с неправильным хэшем ингредиента')
    def test_create_order_with_wrong_ingredient_hash(self, get_access_token, wrong_ingredient_hash):
        response = api.create_order(wrong_ingredient_hash, get_access_token)
        assert response.status_code == 500

    @allure.story('Создание заказа без авторизации')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Тест на создание заказа без токена авторизации')
    def test_create_order_without_auth(self, get_ingredients, empty_auth_token):
        response = api.create_order(get_ingredients, empty_auth_token)
        assert response.status_code == 200

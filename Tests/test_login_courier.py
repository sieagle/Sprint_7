import allure
import pytest
import requests
from datas import ResponseMessages, DatasCourier
from helper import LoginCourier, Helper
from urls import Url
from endpoints import Endpoints

class TestLoginCourier:

    @allure.title('Авторизация курьера с валидными данными')
    @allure.description('Отправлять запрос на авторизацию в сервисе, проверить ответ, удaлить курьера')
    @allure.step('Тест на авторизацию курьера с валидными')
    def test_courier_login(self, courier):
        data_courier = courier["data"]
        with allure.step("Отправить запрос на авторизацию курьера с валидными данными"):
            response = Helper.login_courier_and_get_id(data_courier)
        assert response["status_code"] == 200
        assert response["id"]

    @allure.title('Авторизация курьера с невалидными данными')
    @allure.description('Отправить запрос на авторизацию пользователя с незаполненным обязательными полем и проверить ответ')
    @allure.step('Проверка ошибки при попытке регистрации курьера с валидными данными')
    @pytest.mark.parametrize('login_courier', [LoginCourier.login_wo_login,
                                               LoginCourier.login_wo_pass])
    def test_courier_login_wo_parameters_fail(self, login_courier):
        with allure.step("Отправить запрос на авторизацию курьера с недостающим логином; недостающим паролем"):
            response = requests.post(f'{Url.base_url}{Endpoints.login_courier}', data=login_courier)
        assert response.status_code == 400
        assert ResponseMessages.courier_login_not_enough_data in response.json()["message"]


    @allure.title('Авторизация курьера с несущетвующими данными')
    @allure.description('Отправить запрос на авторизацию с несуществующими данными и проверить ответ')
    @allure.step('Проверка ошибки при попытке авторизации несуществующего курьера')
    def test_courier_login_non_exist_fail(self):
        with allure.step("Отправить запрос на авторизацию несуществующего курьера"):
            response = requests.post(f'{Url.base_url}{Endpoints.login_courier}', data=DatasCourier.login_null)
        assert response.status_code == 404
        assert ResponseMessages.courier_not_found in response.json()["message"]

    @allure.title('Авторизация курьера с некорректными данными логин')
    @allure.description('Отправить запрос на авторизацию пользователя с неверно заполненным обязательными полем и проверить ответ')
    @allure.step('Проверка ошибки авторизации курьера с некорректными данными в поле login')
    def test_courier_login_invalid_login_failed(self, courier):
        data = courier["data"]
        with allure.step("Отправить запрос на авторизацию курьера с неверным логином"):
            response = Helper.login_courier_and_get_id_with_data(data["login"], "test1234")
        assert response["status_code"] == 404
        assert ResponseMessages.courier_not_found in response["response"]["message"]

    @allure.title('Авторизация курьера с некорректным паролем')
    @allure.description('Отправить запрос на авторизацию пользователя с неверно заполненным обязательными полем и проверить ответ')
    @allure.step('Проверка ошибки авторизации курьера с некорректными данными в поле password')
    def test_courier_login_invalid_password_failed(self, courier):
        data = courier["data"]
        with allure.step("Отправить запрос на авторизацию с неверным паролем"):
            response = Helper.login_courier_and_get_id_with_data(data["password"], "test1234")
        assert response["status_code"] == 404
        assert ResponseMessages.courier_not_found in response["response"]["message"]

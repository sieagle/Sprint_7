import allure
import pytest
import requests
from datas import Courier, LoginCourier
from urls import Url
from endpoints import Endpoints


class TestLoginCourier:

    @allure.title('Авторизация курьера с валидными данными')
    @allure.description('Отправлять запрос на авторизацию в сервисе, проверить ответ, удaлить курьера')
    def test_courier_login(self, courier):
        data_courier = courier["data"]
        response = Courier.login_courier_and_get_id(data_courier)
        assert response["status_code"] == 200
        assert response.get("id")

    @allure.title('Авторизация курьера с невалидными данными')
    @allure.description('Отправить запрос на авторизацию пользователя с незаполненным обязательными полем и проверить ответ')
    @pytest.mark.parametrize('login_courier', [LoginCourier.login_wo_login,
                                               LoginCourier.login_wo_pass])
    def test_courier_login_wo_parameters_fail(self, login_courier):
        response = requests.post(f'{Url.base_url}{Endpoints.login_courier}', data=login_courier)
        assert response.status_code == 400
        assert "Недостаточно данных для входа" in response.text


    @allure.title('Авторизация курьера с несущетвующими данными')
    @allure.description('Отправить запрос на авторизацию с несуществующими данными и проверить ответ')
    def test_courier_login_non_exist_fail(self):
        response = requests.post(f'{Url.base_url}{Endpoints.login_courier}', data=LoginCourier.login_null)
        assert response.status_code == 404
        assert "Учетная запись не найдена" in response.text
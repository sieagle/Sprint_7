import allure
import pytest
from helper import Helper
from generate import Generator
from datas import ResponseMessages

class TestCreateHelper:
    @allure.title('Создание нового курьера')
    @allure.description('Создать нового курьера, проверить ответ, удалить созданного курьера')
    def test_registration_courier_valid(self):
        courier = Helper.registration_courier()
        assert courier["status_code"] == 201
        assert courier["response"]["ok"] == True

    @allure.title('Ошибка создания существующего курьера')
    @allure.description('Отправить 2 запроса на создание с одними и теми же данными')
    def test_register_double_failed(self):
        courier = Helper.registration_courier()
        courier_second = Helper.registration_courier_with_data(courier["data"])
        assert courier_second["status_code"] == 409
        assert ResponseMessages.login_already_exists in courier_second["response"]["message"]

    @allure.title('Регистрации без обязательных полей логина/пароля')
    @allure.description('Отправить запрос с незаполненным обязательным полем')
    @pytest.mark.parametrize('datas', [Generator.generate_random_data_wo_login(),
                                       Generator.generate_random_data_wo_password()])
    def test_registrations_with_invalid_data_failed(self, datas):
        courier = Helper.registration_courier_with_data(datas)
        assert courier["status_code"] == 400
        assert ResponseMessages.not_enough_data in courier["response"]["message"]
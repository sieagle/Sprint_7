import requests
import allure
from generate import Generator
from urls import Url
from endpoints import Endpoints

class Helper:
    @staticmethod
    @allure.step('Функция для регистрации курьера с валидными рандомными данными')
    def registration_courier():
        with allure.step("Сгенерировать валидные данные для регистрации курьера"):
            data = Generator.generate_random_valid_data()
        with allure.step("Отправить запрос на регистрацию"):
            response = requests.post(f'{Url.base_url}{Endpoints.create_courier}', data=data)
        return {"response": response.json(), "status_code": response.status_code, "data": data}
    
    @staticmethod
    @allure.step('Функция для регистрации курьера с валидными данными')
    def registration_courier_with_data(data):
        with allure.step("Отправить запрос на регистрацию с кастомными данными"):
            response = requests.post(f'{Url.base_url}{Endpoints.create_courier}', data=data)
        return {"response": response.json(), "status_code": response.status_code, "data": data}
    
    @staticmethod
    @allure.step('Функция для логина курьера и возвратом id курьера')
    def login_courier_and_get_id(data):
        with allure.step("Отправить запрос на авторизацию юзера с кастомными данными и вернуть id курьера"):
            response = requests.post(f'{Url.base_url}{Endpoints.login_courier}', data=data)
        return {"id": str(response.json()["id"]), "response": response.json(), "status_code": response.status_code}
    
    @staticmethod
    @allure.step('Функция для логина курьера и возвратом id курьера со своей датой')
    def login_courier_and_get_id_with_data(login, password):
        with allure.step("Отправить запрос на авторизацию юзера с кастомными логином и паролем и вернуть id курьера"):
            response = requests.post(f'{Url.base_url}{Endpoints.login_courier}', data={
                "login": login,
                "password": password
            })
        return {"response": response.json(), "status_code": response.status_code}
    
    @staticmethod
    @allure.step('Функция для удаления курьера')
    def delete_courier(id):
        with allure.step("Отправить запрос на удаление курьера по id"):
            response = requests.delete(f'{Url.base_url}{Endpoints.delete_courier}{id}')
        return {"response": response.json(), "status_code": response.status_code}
    
class LoginCourier:
    login_validation = Generator.generate_random_valid_data()
    login_wo_login = Generator.generate_random_data_wo_login()
    login_wo_pass = Generator.generate_random_data_wo_password()
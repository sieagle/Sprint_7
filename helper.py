import requests
from generate import Generator
from urls import Url
from endpoints import Endpoints

class Helper:
    # функция для регистрации курьера с валидными рандомными данными
    @staticmethod
    def registration_courier():
        data = Generator.generate_random_valid_data()
        response = requests.post(f'{Url.base_url}{Endpoints.create_courier}', data=data)
        return {"response": response.json(), "status_code": response.status_code, "data": data}
    
    # функция для регистрации курьера с валидными данными
    @staticmethod
    def registration_courier_with_data(data):
        response = requests.post(f'{Url.base_url}{Endpoints.create_courier}', data=data)
        return {"response": response.json(), "status_code": response.status_code, "data": data}
    
    # функция для логина курьера и возвратом id курьера
    @staticmethod
    def login_courier_and_get_id(data):
        response = requests.post(f'{Url.base_url}{Endpoints.login_courier}', data=data)
        return {"id": str(response.json()["id"]), "response": response.json(), "status_code": response.status_code}
    
    # функция для логина курьера и возвратом id курьера со своей датой
    @staticmethod
    def login_courier_and_get_id_with_data(login, password):
        response = requests.post(f'{Url.base_url}{Endpoints.login_courier}', data={
            "login": login,
            "password": password
        })
        return {"response": response.json(), "status_code": response.status_code}

    @staticmethod
    def delete_courier(id):
        response = requests.delete(f'{Url.base_url}{Endpoints.delete_courier}{id}')
        return {"response": response.json(), "status_code": response.status_code}
    
class LoginCourier:
    login_validation = Generator.generate_random_valid_data()
    login_wo_login = Generator.generate_random_data_wo_login()
    login_wo_pass = Generator.generate_random_data_wo_password()
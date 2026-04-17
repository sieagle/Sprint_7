import requests
import random
import string
from urls import Url
from endpoints import Endpoints

def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

class Generator:
    @staticmethod
    def generate_random_valid_data():
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        return payload
    
    @staticmethod
    def generate_random_data_wo_login():
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        payload = {
            "login": "",
            "password": password,
            "firstName": first_name
        }
        return payload
    
    @staticmethod
    def generate_random_data_wo_password():
        login = generate_random_string(10)
        first_name = generate_random_string(10)

        payload = {
            "login": login,
            "password": "",
            "firstName": first_name
        }
        return payload
    
class Courier:
    # функция для регистрации курьера с валидными рандомными данными
    @staticmethod
    def registration_courier():
        data = Generator.generate_random_valid_data()
        response = requests.post(f'{Url.base_url}{Endpoints.create_courier}', data=data)
        return {"response_text": response.text, "status_code": response.status_code, "data": data}
    
    # функция для регистрации курьера с валидными данными
    @staticmethod
    def registration_courier_with_data(data):
        response = requests.post(f'{Url.base_url}{Endpoints.create_courier}', data=data)
        return {"response_text": response.text, "status_code": response.status_code, "data": data}
    
    # функция для логина курьера и возвратом id курьера
    @staticmethod
    def login_courier_and_get_id(data):
        response = requests.post(f'{Url.base_url}{Endpoints.login_courier}', data=data)
        return {"id": str(response.json()["id"]), "response_text": response.text, "status_code": response.status_code}
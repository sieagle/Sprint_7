import string
import random

class Generator:
    
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string
    
    @staticmethod
    def generate_random_valid_data():
        login = Generator.generate_random_string(10)
        password = Generator.generate_random_string(10)
        first_name = Generator.generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        return payload
    
    @staticmethod
    def generate_random_data_wo_login():
        password = Generator.generate_random_string(10)
        first_name = Generator.generate_random_string(10)

        payload = {
            "login": "",
            "password": password,
            "firstName": first_name
        }
        return payload
    
    @staticmethod
    def generate_random_data_wo_password():
        login = Generator.generate_random_string(10)
        first_name = Generator.generate_random_string(10)

        payload = {
            "login": login,
            "password": "",
            "firstName": first_name
        }
        return payload
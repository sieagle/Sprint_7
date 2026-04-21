import allure
import json
import pytest
import requests
from endpoints import Endpoints
from datas import Orderorder
from urls import Url
from datas import ResponseMessages

class TestOrderCreate:

    @allure.title('Оформление заказа с разным набором цветов')
    @allure.description('Отправить запрос на создание заказа с поочередным добавлением разных цветов и проверяем ответ')
    @allure.step('Оформление заказа с разным набором цветов, с двумя выюранными цветами, без цвета')
    @pytest.mark.parametrize('color', [{"color": ["BLACK"]}, {"color": ["GRAY"]}, {"color": ["BLACK", "GRAY"]}, {"color": [""]}])
    def test_create_order_success(self, color):
        headers = {"Content-type": "application/json"}
        data = Orderorder.data
        data.update(color)
        data = json.dumps(data)
        with allure.step("Отправить запрос на заказ самоката"):
            response = requests.post(f'{Url.base_url}{Endpoints.create_order}', headers=headers, data=data)
        assert response.status_code == 201
        assert ResponseMessages.post_create_order in response.json()
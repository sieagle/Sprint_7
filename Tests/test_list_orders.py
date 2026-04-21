import allure
import requests
from urls import Url
from endpoints import Endpoints
from datas import ResponseMessages



class TestListOrder:
    @allure.title('Получение списка заказов')
    @allure.description('Получить списки заказов и проверить ответ')
    @allure.step('Тест на получение списка заказов')
    def test_list_order(self):
        with allure.step("Отправить запрос на получение списка заказов"):
            response = requests.get(f'{Url.base_url}{Endpoints.get_list_order}')
        assert response.status_code == 200
        assert ResponseMessages.get_list_order in response.json()
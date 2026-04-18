import allure
from datas import Courier

class TestCourierDelete:
    @allure.title('Удаление курьера')
    @allure.description('Отправить запрос на удаление курьера и проверить ответ')
    def test_delete_courier(self, courier_delete):
        coorier_id = courier_delete['id']
        response = Courier.delete_courier(coorier_id)
        assert response["status_code"] == 200
        assert response["response_text"] == '{"ok":true}'

    @allure.title('Удаление курьера с несуществующим id')
    @allure.description('Отправить запрос на удаление курьера с несуществующим id и проверить ответ')
    def test_delete_courier_nonexist_id_failed(self):
        coorier_id = '1234567'
        response = Courier.delete_courier(coorier_id)
        assert response["status_code"] == 404
        assert "Курьера с таким id нет" in response["response_text"] 
    
    # @allure.title('Удаление курьера с пустым id')
    # @allure.description('Отправить запрос на удаление курьера с пустым id и проверить ответ')
    # def test_delete_courier_null_id_failed(self):
    #     coorier_id = None
    #     response = Courier.delete_courier(coorier_id)
    #     assert response["status_code"] == 400
    #     assert "Недостаточно данных для удаления курьера" in response["response_text"] 
 

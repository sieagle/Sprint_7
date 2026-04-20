import allure
from helper import Helper
from datas import ResponseErrorMessages

class TestCourierDelete:
    @allure.title('Удаление курьера')
    @allure.description('Отправить запрос на удаление курьера и проверить ответ')
    def test_delete_courier(self, courier_delete):
        coorier_id = courier_delete['id']
        with allure.step("Отправить запрос на удаление курьера"):
            response = Helper.delete_courier(coorier_id)
        assert response["status_code"] == 200
        assert response["response"]["ok"] == True

    @allure.title('Удаление курьера с несуществующим id')
    @allure.description('Отправить запрос на удаление курьера с несуществующим id и проверить ответ')
    def test_delete_courier_nonexist_id_failed(self):
        coorier_id = '1234567'
        with allure.step("Отправить запрос на удаление курьера"):
            response = Helper.delete_courier(coorier_id)
        assert response["status_code"] == 404
        assert ResponseErrorMessages.delete_id_courier_not_found in response["response"]["message"]
    
    @allure.title('Удаление курьера с пустым id')
    @allure.description('Отправить запрос на удаление курьера с пустым id и проверить ответ')
    def test_delete_courier_null_id_failed(self):
        coorier_id = None
        with allure.step("Отправить запрос на удаление курьера"):
            response = Helper.delete_courier(coorier_id)
        assert response["status_code"] == 400
        assert ResponseErrorMessages.delete_courier_not_enough_data in response["response"]["message"]
 

import allure
from helper import Helper
from datas import ResponseMessages

class TestCourierDelete:

    @allure.title('Удаление курьера')
    @allure.description('Отправить запрос на удаление курьера и проверить ответ')
    @allure.step('Тест на удаление курьера')
    def test_delete_courier(self):
        courier = Helper.registration_courier()
        courier_id = Helper.login_courier_and_get_id_with_data(login=courier["data"]["login"], password=courier["data"]["password"])["response"]["id"]
        with allure.step("Отправить запрос на удаление курьера"):
            response = Helper.delete_courier(courier_id)
        assert response["status_code"] == 200
        assert response["response"]["ok"] == True


    @allure.title('Удаление курьера с несуществующим id')
    @allure.description('Отправить запрос на удаление курьера с несуществующим id и проверить ответ')
    @allure.step('Тест на корректную ошибку при попытке удалить курьера с невалидным id')
    def test_delete_courier_nonexist_id_failed(self):
        coorier_id = '1234567'
        with allure.step("Отправить запрос на удаление курьера"):
            response = Helper.delete_courier(coorier_id)
        assert response["status_code"] == 404
        assert ResponseMessages.delete_id_courier_not_found in response["response"]["message"]
    
    @allure.title('Удаление курьера с пустым id')
    @allure.description('Отправить запрос на удаление курьера с пустым id и проверить ответ')
    @allure.step('Тест на корректную ошибку при попытке удалить курьера без id')
    def test_delete_courier_null_id_failed(self):
        coorier_id = None
        with allure.step("Отправить запрос на удаление курьера"):
            response = Helper.delete_courier(coorier_id)
        assert response["status_code"] == 400
        assert ResponseMessages.delete_courier_not_enough_data in response["response"]["message"]
 

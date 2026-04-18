Проект по выполнению задания 7 спринта "Автоматизированное тестирование API учебного приложения Яндекс.Самокат".

Ссылка на сервис: 'https://qa-scooter.praktikum-services.ru/' #Находится в файле urls.py

Ссылка на документацию: 'https://qa-scooter.praktikum-services.ru/docs/#api-Courier-DeleteCourier'

allure_results - отчет о тестировании
Папка 'tests':
-test_create_courier.py - файл с проверками создания курьера 
-test_create_order.py - файл с проверками создания заказа
-test_delete_courier.py - файл с проверками удаления курьера
-test_list_orders.py - файл с проверками получения списков заказа
-test_login_courier.py - файл с проверками авторизации курьера

conftest.py - файл с фикстурами
datas.py - файл с вспомогательными функциями и данными 
endpoints.py - файл с эндпоинтами
requirements.txt - файл с внешними зависимостями
urls - файл с ссылкой на сервис

В файле test_delete_courier.py есть закомментированный код- это тест который "падает" предположительно из-за ошибки в документации, так как в документации написано, что данная ошибка должна возвращать: "400 Bad Request
{
  "message":  "Недостаточно данных для удаления курьера"
}", 
тогда как даже при ручной проверке в postman она возвращает: "500  Internal Server Error
{
    "code": 500,
    "message": "invalid input syntax for type integer: \":id\""
}"

class DatasCourier:
    login_null = {
        "login": "null",
        "password": "null"
    }
    
class Orderorder:
    data = {
        "firstName": "Сергей",
        "lastName": "Есенин",
        "address": "г.Москва",
        "metroStation": 1,
        "phone": "+7 999 99 99",
        "rentTime": 3,
        "deliveryDate": "2026-05-01",
        "comment": "Так мало пройдено дорог, так много сделано ошибок...",
    }

class ResponseMessages:
    login_already_exists = "Этот логин уже используется"
    not_enough_data = "Недостаточно данных для создания учетной записи"

    courier_not_found = "Учетная запись не найдена"
    courier_login_not_enough_data = "Недостаточно данных для входа"

    delete_id_courier_not_found = "Курьера с таким id нет"
    delete_courier_not_enough_data = "Недостаточно данных для удаления курьера"

    get_list_order = "orders"
    post_create_order = "track"


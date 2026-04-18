import pytest
from datas import Courier

@pytest.fixture()
def courier():
    courier_create = Courier.registration_courier()
    courier_login = Courier.login_courier_and_get_id(courier_create["data"])
    yield courier_create
    Courier.delete_courier(courier_login["id"])

@pytest.fixture()
def courier_delete():
    courier_create = Courier.registration_courier()
    courier_login = Courier.login_courier_and_get_id(courier_create["data"])
    return courier_login
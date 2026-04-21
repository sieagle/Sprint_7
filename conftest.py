import pytest
from helper import Helper

@pytest.fixture()
def courier():
    courier_create = Helper.registration_courier()
    courier_login = Helper.login_courier_and_get_id(courier_create["data"])
    yield courier_create
    Helper.delete_courier(courier_login["id"])

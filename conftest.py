import allure
import pytest
import requests
import data
from samokat_api import ScooterApi
import helper
from urls import Urls


@allure.step("Создание шаблонного курьера")
@pytest.fixture(scope='function')
def default_courier(payload):
    samokat_response = ScooterApi().create_courier(data.TestDataCourier.create_courier_payload(payload))
    yield samokat_response


    response_id = requests.post(Urls.BASE_URL+Urls.AUTH_URL,data=payload)
    id_number=response_id.json()["id"]
    response_delete=requests.delete(f"{Urls.BASE_URL+Urls.DELETE_URL}{id_number}")
    return response_delete





import allure
import pytest

import data
import allure
import pytest

import data
import samokat_api
import helper
from urls import Urls


@allure.step("Создание шаблонного курьера")
@pytest.fixture(scope='function')
def default_booking(payload):
    samokat_response = samokat_api.SamokatApi.create_courier(data.TestDataCourier.create_courier_payload(payload))


    yield samokat_response


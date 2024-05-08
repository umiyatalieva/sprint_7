import requests
import pytest

import data
import helper
from samokat_api import SamokatApi
from data import TestDataCreateOrder
import allure

class TestCreateOrder:
    @allure.title("Проверка успешности создания заказа")
    @allure.description("Создание шаблонного заказа, проверка статуса ответа ")
    @allure.title("Проверка успешного создания заказа с указанием разных вариантов цвета")
    @pytest.mark.parametrize("color", [
        pytest.param(['BLACK']),
        pytest.param(['']),
        pytest.param(['BLACK','GREY'])
    ])
    def test_success_create_booking_with_different_totalprice(self, color):
        body = data.TestDataCreateOrder.CREAT_ORDER_DATA("color", color)
        created_booking_request = SamokatApi.create_order(body)
        assert (created_booking_request.status_code == 200 and created_booking_request.text == 'track')




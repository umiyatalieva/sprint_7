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
    @pytest.mark.parametrize('ORDER_DATA',TestDataCreateOrder.ORDER_DATA)
    def test_creat_order(self, ORDER_DATA):
        creat_order_request = SamokatApi().create_order(data.TestDataCreateOrder.ORDER_DATA)
        assert creat_order_request.status_code == 201
        print(creat_order_request.text)






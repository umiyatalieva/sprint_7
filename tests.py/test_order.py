import requests
import pytest
import data
import helper
from samokat_api import ScooterApi
from data import TestDataCreateOrder
import allure
import json

class TestCreateOrder:
    @allure.title("Проверка успешности создания заказа")
    @allure.description("Создание шаблонного заказа, проверка статуса ответа ")
    @allure.title("Проверка успешного создания заказа с указанием разных вариантов цвета")
    @pytest.mark.parametrize('ORDER_DATA',TestDataCreateOrder.ORDER_DATA)
    def test_creat_order(self, ORDER_DATA):
        creat_order_request = ScooterApi().create_order(data.TestDataCreateOrder.ORDER_DATA)
        assert creat_order_request.status_code == 201
        print(creat_order_request.text)


    def test_list_get_orders(self):
        list_orders_request = ScooterApi().get_list_orders()
        assert  list_orders_request.status_code == 200
        print(list_orders_request.text)






import requests
import allure
import pytest

import data
from urls import Urls
import helper
from data import TestDataAuth
from data import TestDataCreateOrder
from data import TestIdenticalCourier


class SamokatApi:
    @allure.step("Авторизация курьера")
    def auth(self):
        return requests.post(Urls.BASE_URL + Urls.AUTH_URL, json=TestDataAuth.AUTH_DATA_COURIER)
    @allure.step("Создание заказа")
    def  create_order(self):
        resource = requests.post(Urls.BASE_URL + Urls.ORDER_URL, json=TestDataCreateOrder.CREAT_ORDER_DATA)
        return resource
    @allure.step("Создание курьера")
    def create_courier(self,payload):
        return requests.post(Urls.BASE_URL + Urls.COURIER_URL, json = data.TestDataCourier.create_courier_payload(payload))

    @allure.step("Создание  шаблона курьера ")
    def creat_identical_courier(self):
        return requests.post(Urls.BASE_URL + Urls.COURIER_URL , json = data.TestIdenticalCourier.BODY_INDETICAL_COURIER)




    @staticmethod
    @allure.step("Отправка запроса на удаление курьера")
    def delete_booking(id):
        return requests.delete(Urls.BASE_URL + Urls.COURIER_URL + str(id), headers={
            "id":""  + str(SamokatApi.auth())
        })
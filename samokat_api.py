import allure
import requests
import data
import helper
from urls import Urls
import pytest
from data import TestDataAuth
from data import TestDataCreateOrder
from data import TestIdenticalCourier


class SamokatApi:
    @allure.step("Авторизация курьера")
    def auth(AUTH_DATA_COURIER):
        return requests.post(Urls.BASE_URL + Urls.AUTH_URL, json=data.TestDataAuth().AUTH_DATA_COURIER)


    @allure.step("Создание заказа")
    def  create_order(self,ORDER_DATA):
        return requests.post(Urls.BASE_URL + Urls.ORDER_URL, json = ORDER_DATA)



    @allure.step("Создание курьера")
    def create_courier(self,payload):
        return requests.post(Urls.BASE_URL + Urls.COURIER_URL, json = payload)


    @allure.step("Создание  шаблона курьера ")
    def creat_identical_courier(self):
        return requests.post(Urls.BASE_URL + Urls.COURIER_URL , json = data.TestIdenticalCourier.BODY_INDETICAL_COURIER)



    @allure.step("Создание метода для пустого логина")
    def create_courier_empty_payload(self, param_name):
        payload = helper.create_courier_payload()
        payload[param_name] = ""
        return payload


    @allure.step("Создание метода для одинакового логина")
    def create_courier_indetikal_payload(self, param_name):
        payload = helper.create_courier_payload()
        payload[param_name] = "vika"
        return payload



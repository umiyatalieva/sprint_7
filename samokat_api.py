import allure
import requests
import data
import helper
from urls import Urls
import pytest
from data import TestDataAuth
from data import TestDataCreateOrder
from data import TestIdenticalCourier
from data import TestDataCourier


class ScooterApi:
    @allure.step("Авторизация курьера")
    def auth(self):
        return requests.post(Urls.BASE_URL + Urls.AUTH_URL, json= data.TestDataAuth.AUTH_DATA_COURIER)


    @allure.step("Авторизация курьера если одного поля нет")
    def auth_one_failed(self):
        return requests.post(Urls.BASE_URL + Urls.AUTH_URL, json= data.TestDataAuth.AUTH_DATA_COURIER_NOT_FAILED)


    @allure.step("Авторизация курьера с неправильными данными")
    def auth_invalid_login(self):
        return requests.post(Urls.BASE_URL + Urls.AUTH_URL, json= data.TestDataAuth.AUTH_DATA_COURIER_INVALID_LOGIN)


    @allure.step("Авторизация курьера,если логин некорректный")
    def auth_invalid_one_failed(self):
        return requests.post(Urls.BASE_URL + Urls.AUTH_URL, json= data.TestDataAuth.AUTH_DATA_COURIER_INVALID_ONE_FAILED)


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


    @allure.step("Получение списка заказов")
    def get_list_orders(self):
        return requests.get(Urls.BASE_URL+Urls.ORDER_URL)



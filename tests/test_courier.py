import requests
import pytest
import allure
import helper
from samokat_api import SamokatApi
import data

class TestCreateBooking:
    @allure.title("Проверка успешности создания курьера")
    @allure.description("Создание шаблонного курьера, проверка  корректного статуса ответа и тело ответа возвращает правильное")
    def test_success_create_booking(self):
        created_courier_request = SamokatApi.create_courier(data.TestDataCourier.create_courier_payload())
        assert created_courier_request == 200
    @allure.title("Проверка  на ошибку при создании двух одинаковых курьеров ")
    @allure.description("Сохдание двух одинаковых курьеров и проверка статуса ответа")
    def test_creat_two_Identical_courier(self):
        created_courier_request = SamokatApi.creat_identical_courier(data.TestIdenticalCourier.BODY_INDETICAL_COURIER)
        created_courier_request_two = SamokatApi.creat_identical_courier(data.TestIdenticalCourier.BODY_INDETICAL_COURIER)
        assert created_courier_request_two.status_code == 409

    @allure.title("Проверка  на ошибку при создании , без одного обязательного поля ")
    @allure.description("Сохдание курьера без одного обязательного поля и проверка что запрос вернет  ошибку")
    def test_creat_two_Identical_courier(self):
        body = data.TestDataCourier.create_courier_payload("login","")
        created_courier_request = SamokatApi.create_courier(body)
        assert created_courier_request.status_code == 400

    @allure.title("Проверка  на ошибку при создании курьеров с одинаковым логином ")
    @allure.description("Сохдание  курьеров с одинаковым логином и проверка что запрос вернет  ошибку")
    def test_creat_two_Identical_courier(self):
        body = data.TestDataCourier.create_courier_payload("login", "vika")
        created_courier_request = SamokatApi.create_courier(body)
        assert created_courier_request.status_code == 400













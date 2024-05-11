import requests
import pytest
import allure
import helper
from samokat_api import ScooterApi
import data
from urls import Urls
from data import TestDataCourier


class TestCreateCourier:
    @allure.title("Проверка успешности создания курьера")
    @allure.description("Создание шаблонного курьера, проверка  корректного статуса ответа и тело ответа возвращает правильное")
    def test_success_create_courier(self):
        created_courier_request = ScooterApi().create_courier(data.TestDataCourier().create_courier_payload())
        assert created_courier_request.status_code == 201


    @allure.title("Проверка  на ошибку при создании двух одинаковых курьеров ")
    @allure.description("Создание двух одинаковых курьеров и проверка статуса ответа")
    def test_create_two_identical_courier(self):
        payload = data.TestDataCourier().create_courier_payload()
        first_response = ScooterApi().create_courier(payload)
        second_response = ScooterApi().create_courier(payload)

        assert (second_response.status_code == 409 and
                second_response.json()['message'] == 'Этот логин уже используется. Попробуйте другой.')

    @allure.title("Проверка  на ошибку при создании курьера, без одного обязательного поля ")
    @allure.description("Сохдание курьера без одного обязательного поля и проверка что запрос вернет  ошибку")
    def test_create_bad_data_courier(self):
        body = ScooterApi().create_courier_empty_payload("login")
        response = ScooterApi().create_courier(body)

        assert (response.status_code == 400 and
                response.json()['message'] == 'Недостаточно данных для создания учетной записи')


    @allure.title("Проверка  на ошибку при создании курьеров с одинаковым логином ")
    @allure.description("Создание  курьеров с одинаковым логином и проверка что запрос вернет  ошибку")
    def test_creat_two_Identical_courier(self):
        body = ScooterApi().create_courier_indetikal_payload("login")
        response = ScooterApi().create_courier(body)
        assert (response.status_code == 409 and
                response.json()["message"] == 'Этот логин уже используется. Попробуйте другой.')














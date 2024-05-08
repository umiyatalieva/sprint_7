import requests
import allure

import data
import helper
from data import TestDataAuth
from samokat_api import SamokatApi

class TestLoginCourier:
    @allure.title("Проверка  на корректную авторизацию курьеров ")
    @allure.description("Проверяем что курьер авторизуется приуказании всех обязательных "
                        "полей ,а так же тело ответа возвращает его ID")
    def test_login_courier(self):
        login_courier_request = SamokatApi.auth(data.TestDataAuth.AUTH_DATA_COURIER)
        assert login_courier_request.status_code == 200

    @allure.title("Проверка  система вернёт ошибку, если неправильно указать логин или пароль ")
    @allure.description("Проверяем  если неправильно указать логин запрос вернет код ошибку")
    def test_login_courier_invalid_login(self):
        login_courier_request = SamokatApi.auth("login", "dfdg")
        assert login_courier_request.status_code == 404

    @allure.title("Проверка  система вернёт ошибку, если не указать логин или пароль ")
    @allure.description("Проверяем  если не указать логин запрос вернет код ошибку")
    def test_login_courier_not_own_failed(self):
        login_courier_request = SamokatApi.auth("login","")
        assert login_courier_request.status_code == 400


    @allure.title("Проверка  система вернёт ошибку, если авторизоваться под несуществующим пользователем ")
    @allure.description("Проверяем  если авторизоваться под несуществующим пользователем запрос вернет код ошибку")
    def test_login_courier_non_existent(self):
        login_courier_request = SamokatApi.auth(("login","vvvv"),("password","0000"))
        assert login_courier_request.status_code == 404

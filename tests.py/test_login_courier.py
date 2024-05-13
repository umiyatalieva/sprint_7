import pytest
import requests
import allure
import helper
from data import TestDataAuth
from samokat_api import ScooterApi
from urls import Urls
import json
import conftest

class TestLoginCourier:
    @allure.title("Проверка  на корректную авторизацию курьеров ")
    @allure.description("Проверяем что курьер авторизуется при указании всех обязательных полей ,а так же тело ответа возвращает его ID")
    def test_login_courier(self):
        response = ScooterApi().auth()
        assert response.status_code == 200 and response.json()["id"] is not None



    @allure.title("Проверка если какого-то поля нет, запрос возвращает ошибку ")
    @allure.description(" Проверяем ,что при отсутствии логина,возвращается ошибка и сообщение об ошибке 'Недостаточно данных для входа'")
    def test_non_one_field(self):
        response = ScooterApi().auth_one_failed()
        assert response.status_code == 400 and response.json()["message"] == 'Недостаточно данных для входа'


    @allure.title("Проверка , если авторизоваться под несуществующим пользователем, запрос возвращает ошибку")
    @allure.description("Проверяем ,что при отсутствии логина,возвращается ошибка и сообщение об ошибке 'Учетная запись не найдена'")
    def test_invalid_login(self):
        response = ScooterApi().auth_invalid_login()
        assert response.status_code == 404 and response.json()["message"] == 'Учетная запись не найдена'


    @allure.title("Проверка если неправильно указать логин или пароль ,система вернет ошибку ")
    @allure.description("Проверяем ,что при отсутствии логина,возвращается ошибка и сообщение об ошибке 'Учетная запись не найдена'")
    def test_invalid_one_failed(self):

        response = ScooterApi().auth_invalid_one_failed()
        assert response.status_code == 404 and response.json()["message"] == 'Учетная запись не найдена'












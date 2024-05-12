import allure
import pytest
import requests
import data
from samokat_api import ScooterApi
import helper
from urls import Urls


@allure.step("Создание шаблонного курьера")
@pytest.fixture(scope='function')
def default_courier():
    # создаём список, чтобы метод мог его вернуть
    login_pass = []

    login = default_courier(10)
    password = default_courier(10)
    first_name = default_courier(10)

    # собираем тело запроса
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post(Urls.BASE_URL + Urls.COURIER_URL, data=payload)

    # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)
    samokat_response = ScooterApi().create_courier(helper.create_courier_payload(payload))

    yield samokat_response

    response_id = requests.post(Urls.BASE_URL+Urls.AUTH_URL, data=payload)
    id_number = response_id.json()["id"]
    requests.delete(f"{Urls.BASE_URL+Urls.DELETE_URL}{id_number}")






import pytest
import requests
import string
import random
import allure
from urls import Urls


@allure.title('Генерируем курьера')
@allure.step('Создаем метод для рандомного создания курьера')
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string
# создаём список, чтобы метод мог его вернуть
login_pass = []

login = generate_random_string(10)
password = generate_random_string(10)
first_name = generate_random_string(10)
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
@allure.step('Создаем метод для тела зароса')
def create_courier_payload():
    payload = {
        'firstName': generate_random_string(length=10),
        'login': generate_random_string(length=10),
        'password': generate_random_string(length=10)
    }
    return payload


# возвращаем список


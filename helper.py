import requests
import string
import random
import allure
from urls import Urls

def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


@allure.step('Создаем метод для тела зароса')
def create_courier_payload():
     payload = {
        'firstName': generate_random_string(length=10),
        'login': generate_random_string(length=10),
        'password': generate_random_string(length=10)
       }
     return payload


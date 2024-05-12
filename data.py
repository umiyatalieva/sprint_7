import helper
class TestDataCreateOrder:
    ORDER_DATA = [{
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "BLACK"
    ]
},
        {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": [
                "BLACK","GREY"
            ] },

        {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": [
                ""
            ]}]


class TestDataAuth:
    AUTH_DATA_COURIER = {
                "login": "okmn",
                "password": "9512"
            }

    AUTH_DATA_COURIER_NOT_FAILED={
            "login": "",
            "password": "9512"
        }
    AUTH_DATA_COURIER_INVALID_LOGIN={
            "login": "yyyy",
            "password": "0000"
        }
    AUTH_DATA_COURIER_INVALID_ONE_FAILED={
            "login": "yyyy",
            "password": "9512"
        }

class TestIdenticalCourier:

         BODY_INDETICAL_COURIER= {
    "login": "nina",
    "password": "8523",
    "firstName": "yuio"
}







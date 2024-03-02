import requests
import json

class APIException(Exception):
    def __init__(self, message):
        self.message = message

class CurrencyConverter:
    @staticmethod
    def get_price(base, quote, amount):
        try:
            url = f'https://api.exchangerate-api.com/v4/latest/{base}'
            response = requests.get(url)
            data = json.loads(response.text)
            rate = data['rates'][quote]
            converted_amount = float(amount) * rate
            return converted_amount
        except KeyError:
            raise APIException("Неправильно введены валюты")
        except ValueError:
            raise APIException("Неправильно введено количество")

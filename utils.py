import requests
import json
from config import keys

class ConvertionException(Exception):
    pass

class Converter:
    @staticmethod
    def covert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException(f'невозможно перевести одинаковую валюту {base}')

        try:
            quote_tiker = keys[quote]
        except KeyError:
            raise (f'не удалось обработать валюту {quote}')
        try:
            base_tiker = keys[base]
        except KeyError:
            raise (f'не удалось обработать валюту {base}')

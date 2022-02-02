import requests


def currency_rates(code: str) -> float:
    """возвращает курс валюты `code` по отношению к рублю"""
    # ваша реализация здесь
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = requests.utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    code_indx = content.find(code.upper())
    if code_indx != -1:
        start_tag = content.find('<Value>', code_indx)
        finish_tag = content.find('</Value>', start_tag)
        value_length = 7
        result_value = float(content[start_tag + value_length:finish_tag].replace(",", "."))
        return result_value
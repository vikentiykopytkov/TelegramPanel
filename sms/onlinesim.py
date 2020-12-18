import requests
import json

class ONLINESIM_API:
    # Инициализация класса для работы с API onlinesim.ru
    def __init__(self, API_KEY, COUNTRY = 7):
        self.api_key = API_KEY # Ключ API
        self.country = COUNTRY # Код страны

    # Получить баланс
    def get_balance(self):
        preresult = requests.get('https://onlinesim.ru/api/getBalance.php?apikey={0}'.format(self.api_key, self.country))
        result = json.loads(preresult.text)
        return result ['balance']

    # Получить статистику свободных номеров
    def get_stats(self):
        preresult = requests.get('https://onlinesim.ru/api/getNumbersStats.php?apikey={0}&country={1}'.format(self.api_key, self.country))
        result = json.loads(preresult.text)
        return result ['services']

    # Получить статистику свободных номеров для телеграма
    def get_telegram_stats(self):
        preresult = requests.get('https://onlinesim.ru/api/getNumbersStats.php?apikey={0}&country={1}'.format(self.api_key, self.country))
        result = json.loads(preresult.text)
        return result ['services'] ['service_telegram']

    # Получить виртуальный номер (service из get_SMS_API_stats (slug))
    def get_number(self, service: str):
        preresult = requests.get('https://onlinesim.ru/api/getNum.php?apikey={0}&country={1}&service={2}&number=True'.format(self.api_key, self.country, service))
        result = json.loads(preresult.text)
        return result

    def get_state(self, tzid):
        preresult = requests.get('https://onlinesim.ru/api/getState.php?apikey={0}&tzid={1}&message_to_code=1'.format(self.api_key, tzid))
        result = json.loads(preresult.text)
        return result
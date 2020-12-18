import smsapi
from telegram import tgclient
import settings
import random
import time

class AUTOREGISTRATION:
    def __init__(self, API_ID: int, API_HASH: str, session_id: str):
        self.api_id = API_ID
        self.api_hash = API_HASH
        self.sid = session_id
        self.api = smsapi.ONLINESIM_API(API_KEY = settings.API_KEY)
        self.accounts = []

    def create_accounts(self, amount = 1, proxy = 1):
        last_num = sum(self.accounts)
        for i in range(0, amount):
            flag = True
            number = self.api.get_number('telegram')
            phone_number = number['number']
            tzid = number['tzid']
            last_num += random.randint(0, 100)
            try:
                telegram = tgclient.TELEGRAM_CLIENT(
                    id=self.api_id,
                    hash=self.api_hash,
                    session_name=self.sid+'_'+str(last_num),
                    phone_number=phone_number
                    )
            except:
                print('Phone has been banned')
                break
            while flag:
                time.sleep(1)
                state = self.api.get_state(tzid)
                print(state)
                if state [0] ['response'] == 'TZ_NUM_WAIT':
                    pass
                else:
                    code = state [0] ['msg']
                    flag = False
            telegram.enter_code(code)
            print(telegram.get_me())
            self.accounts.append(telegram)

    def get_account(self):
        number = api.get_number('telegram')
        phone_number = number['number']
        tzid = number['tzid']
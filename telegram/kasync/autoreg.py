from sms import onlinesim
from telegram.kasync import tgclient
import settings
import asyncio
import random
import time

class AUTOREGISTRATION:
    def __init__(self, API_ID: int, API_HASH: str, session_id: str):
        self.api_id = API_ID
        self.api_hash = API_HASH
        self.sid = session_id
        self.sms = onlinesim.ONLINESIM_API(API_KEY = settings.API_KEY)
        self.accounts = []

    async def create_accounts(self, reg_data: list = [['Ivan', 'Ivanov']], amount = 1, proxy = 1):
        async def awaiting_code(api, tzid: int, timeout: int = 60):
            while flag:
                if timeout:
                    asyncio.sleep(1)
                    state = api.get_state(tzid)
                    print(state)
                    if state [0] ['response'] == 'TZ_NUM_WAIT':
                        pass
                    else:
                        return {'response': 1,
                                'code': state [0] ['msg']}
                    timeout += -1
                else:
                    return {'response': False,
                            'error': 'SMSTimeout'}
                
        last_num = sum(self.accounts)
        
        for i in range(0, amount):
            flag = True
            number = self.sms.get_number('telegram')
            
            if number ['response'] == 'WARNING_LOW_BALANCE':
                return {'response': False,
                        'error': 'SMSNoBalance'}
            
            phone_number, tzid = number['number'], number['tzid']
            last_num += random.randint(0, 100)
            session = self.sid + '_' + str(last_num)

            telegram = tgclient.TELEGRAM_CLIENT(
                id=self.api_id,
                hash=self.api_hash,
                session_name=session,
                phone_number=phone_number
                )

            if telegram.code_sent:
                code = await awaiting_code(api=self.sms, tzid=tzid)
                if code ['response']:
                    await telegram.enter_code(code ['code'],
                                              reg_data=reg_data[i])
                    if await telegram.is_auth() ['response']:
                        self.accounts.append({'session': session,
                                            'phone': phone_number})
                        if await telegram.change_username(username=session) ['response']:
                            await telegram.close_connection()
                            print('reg-success')

                else:
                    print('reg-er: ' + code ['error'])
            else:
                print('reg-er: phone banned')
        return {'response': 1}

    async def get_account(self, session: dict):
        telegram = tgclient.TELEGRAM_CLIENT(
            id=self.api_id,
            hash=self.api_hash,
            session_name=session ['session'],
            phone_number=session ['phone']
            )
        return await telegram.get_me()
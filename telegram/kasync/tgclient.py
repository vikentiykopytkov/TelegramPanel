from telethon import TelegramClient
from telethon import functions, types
from telethon.errors.rpcerrorlist import PhoneNumberOccupiedError
import socks
import asyncio

class TELEGRAM_CLIENT:
    def __init__(self, id: int, hash: str, session_name: str, phone_number: str, proxy = None):
        self.api_id = id
        self.api_hash = hash
        self.session_name = session_name
        self.phone_number = phone_number

        self.client = TelegramClient(self.session_name,
                                     self.api_id,
                                     self.api_hash,
                                     proxy = proxy)

        await self.client.connect()

        if not await self.client.is_user_authorized():
            try:
                await self.client.send_code_request(self.phone_number)
                print('Code sent to ' + self.phone_number)
                self.code_sent = 1
            except:
                self.code_sent = 0

    async def close_connection(self):
        try:
            await self.client.disconnect()
            return {'response': 1}
        except:
            return {'response': False}

    async def is_auth(self):
        if not await self.client.is_user_authorized():
            return {'response': False}
        else:
            return {'response': 1}

    async def enter_code(self, code, reg_data: list = ['Ivan', 'Ivanov']):
        try:
            self.me = await self.client.sign_up(code=code,
                                                first_name=reg_data[0],
                                                last_name=reg_data[1])
            if not await self.client.is_user_authorized():
                return {'response': False}
            else:
                return {'response': 1}
        except telethon.errors.rpcerrorlist.PhoneNumberOccupiedError:
            self.me = await self.client.sign_in(self.phone_number, code)
            if not await self.client.is_user_authorized():
                return {'response': False}
            else:
                return {'response': 1}

    async def edit_2FA(self, new_password: str, current_password = None):
        try:
            if not current_password:
                await self.client.edit_2fa(new_password=new_password)
            else:
                await self.client.edit_2fa(current_password=current_password,
                                           new_password=new_password)
            return {'response': 1}
        except:
            return {'response': False}

    async def clear_2FA(self, current_password: str):
        try:
            await self.client.edit_2fa(current_password=current_password,
                                       new_password=None)
            return {'response': 1}
        except:
            return {'response': False}

    async def get_me(self):
        try:
            client_me = await self.client.get_me().stringify()
            return {'response': 1,
                    'client_me': client_me}
        except:
            return {'response': False, 'ban': 1}

    async def change_username(self, username: str):
        try:
            result = await self.client(functions.account.UpdateUsernameRequest(
                        username=username
                        ))
            return {'response': 1,
                    'result': result.stringify()}
        except:
            return {'response': False}
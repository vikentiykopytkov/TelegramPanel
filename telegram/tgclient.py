from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import PhoneNumberOccupiedError

class TELEGRAM_CLIENT:
    def __init__(self, id: int, hash: str, session_name: str, phone_number: str):
        self.api_id = id
        self.api_hash = hash
        self.session_name = session_name
        self.phone_number = phone_number

        self.client = TelegramClient(self.session_name, self.api_id, self.api_hash)

        self.client.connect()

        if not self.client.is_user_authorized():
            self.client.send_code_request(self.phone_number)
            print('Code sent to ' + self.phone_number)
            return {'response': False}
        
        return {'response': 1}

    def is_auth(self):
        if not self.client.is_user_authorized():
            return {'response': False}
        else:
            return {'response': 1}

    def enter_code(self, code, reg_data: list = ['Ivan', 'Ivanov']):
        try:
            self.me = self.client.sign_up(code=code,
                                          first_name=reg_data[0],
                                          last_name=reg_data[1])
            if not self.client.is_user_authorized():
                return {'response': False}
            else:
                return {'response': 1}
        except telethon.errors.rpcerrorlist.PhoneNumberOccupiedError:
            self.me = self.client.sign_in(self.phone_number, code)
            if not self.client.is_user_authorized():
                return {'response': False}
            else:
                return {'response': 1}

    def edit_2FA(self, new_password: str, current_password = None):
        try:
            if not current_password:
                self.client.edit_2fa(new_password=new_password)
            else:
                self.client.edit_2fa(current_password=current_password,
                                     new_password=new_password)
            return {'response': 1}
        except:
            return {'response': False}

    def clear_2FA(self, current_password: str):
        try:
            self.client.edit_2fa(current_password=current_password,
                                 new_password=None)
            return {'response': 1}
        except:
            return {'response': False}

    def get_me(self):
        try:
            client_me = self.client.get_me().stringify()
            return {'response': 1,
                    'client_me': client_me}
        except:
            return {'response': False}
        
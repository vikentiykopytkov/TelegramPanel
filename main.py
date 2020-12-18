import settings
import telegram
import smsapi

ar = telegram.autoreg.AUTOREGISTRATION(
    API_ID=settings.API_ID,
    API_HASH=settings.API_HASH,
    session_id='debug'
    )

if __name__ == '__main__':
    response = ar.create_accounts()
    if response ['response']:
        print(ar.accounts)
        print(ar.get_account(ar.accounts[0]))
    else:
        print('Error: ' + response ['error'])
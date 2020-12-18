import settings
import telegram
import time

ar = telegram.autoreg.AUTOREGISTRATION(
    API_ID=settings.API_ID,
    API_HASH=settings.API_HASH,
    session_id='debug'
    )

if __name__ == '__main__':
    names = [
        ['Василий', 'Акилов'],
        ['Дмитрий', 'Иванов'],
        ['Илья', 'Желудов']
        ]
    response = ar.create_accounts(amount=1,
                                  proxy=3,
                                  reg_data=names)
    if ar.accounts:
        print(ar.accounts)
        print(ar.get_account(ar.accounts[0]))
    else:
        print('Error: ' + response ['error'])
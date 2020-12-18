import settings
import telegram
import smsapi

ar = telegram.autoreg.AUTOREGISTRATION(
    API_ID=settings.API_ID,
    API_HASH=settings.API_HASH,
    session_id='first_test'
    )

ar.create_accounts()
print(ar.accounts)

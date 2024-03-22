from .melipayamak import Api
from .models import OTP
import random
from datetime import datetime, timedelta
from django.conf import settings

username = settings.SMS_USER
password = settings.SMS_PASS

panel_number = '50004001488817'
api = Api(username,password)


def genrate_code():
    return random.randint(10000,99999)

def send_sms(user, req_otp_type ):
    code = genrate_code()
    expire_time = datetime.now() + timedelta(minutes=2)
    otp = OTP(user=user,code=code,active=False,otp_type=req_otp_type,expire_time=expire_time)
    otp.save()
    text = f'کد شما: {code}'
    response = api.send(user.phone_number,panel_number,text)



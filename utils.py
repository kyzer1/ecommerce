from kavenegar import *
from django.contrib.auth.mixins import UserPassesTestMixin


def send_otp_code(phone_number, code):
    try:
        api = KavenegarAPI('34376F4B2B7569566657484C44356335336B716A516644516263674E504C617570795272424E5337594A343D')
        params = {
            'sender': '',
            'receptor': phone_number,
            'message': f'کد تایید شما  { code }'
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e: 
        print(e)
    except HTTPException as e: 
        print(e)


class IsAdminUserMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_admin
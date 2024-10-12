from typing import List, Dict
from aiohttp import web

from openapi_server.models.demo_auth_response import DemoAuthResponse
from openapi_server.models.demo_auth_verify_response import DemoAuthVerifyResponse
from openapi_server.models.get_device_code_id401_response import GetDeviceCodeId401Response
from openapi_server.models.signupid400_response import SIGNUPId400Response
from openapi_server.models.verify_account_id500_response import VerifyAccountId500Response
from openapi_server.models.verify_otpid400_response import VerifyOTPId400Response
from openapi_server import util


async def s_ign_up_id(request: web.Request, clientid=None, consent=None, demoauth=None, dob=None, gender=None, hmac=None, mobile=None, name=None, ts=None, uid=None, verification=None) -> web.Response:
    """SIGN UP

    This API is used to validate Aadhaar details and verify the mobile number by generating an OTP. This API call, if successful, will be followed by verify OTP call by the partner application if the user is online or available to perform OTP validation as indicated in verification parameter

    :param clientid: Provide the client id that was created during the application registration process on Partners Portal.
    :type clientid: str
    :param consent: The consent indicator from the user for performing demographic authentication using Aadhaar details. This Partner Application must capture the user consent for performing the Aadhaar demographic authentication. The possible values are ‘Y’ and ‘N’. The sign up request will be processed only when this indicator is ‘Y’.
    :type consent: str
    :param demoauth: The parameter indicates whether Aadhaar demographic authentication must be successful for creating DigiLocker account. The possible values are ‘Y’ and ‘N’. The value of ‘Y’ will perform Aadhaar demographic authentication and will return errors if any in response. The value of ‘N’ will also perform Aadhaar demographic authentication but will return any error in case of authentication failure. It will create a basic mobile based account for the user. Value ‘N’ should be used when the user account needs to be created in the absence of the user.
    :type demoauth: str
    :param dob: This is date of birth of the user as mentioned in Aadhaar in DDMMYYYY format.
    :type dob: int
    :param gender: This is gender of the user as mentioned in Aadhaar. The possible values are M, F, T for male, female and transgender respectively.
    :type gender: str
    :param hmac: Provide SHA-256 encrypted value of the client secret, clientid and ts parameters above concatenated in this sequence (client secret, clientid, ts). The hmac parameter is used by DigiLocker to ensure the data integrity and authentication of the request. Use the Client Secret Key generated during the application registration process on Partners Portal as the client secret.
    :type hmac: str
    :param mobile: This is the mobile number of the user. DigiLocker will check whether an account exists for this mobile number. Either uid or mobile is required to verify whether an account exists.
    :type mobile: int
    :param name: This is name of the user as mentioned in Aadhaar.
    :type name: str
    :param ts: Provide a timestamp value in UNIX (or POSIX) format in IST time zone in seconds. This timestamp value must not be older than 30 minutes.
    :type ts: str
    :param uid: This is the Aadhaar number of the user. DigiLocker will check whether an account exists for this Aadhaar number. Either uid or mobile is required to verify whether an account exists.
    :type uid: int
    :param verification: The parameter indicates whether the mobile number provided above should be validated by DigiLocker. If this parameter is ‘Y’, the DigiLocker sends an OTP to verify the mobile number. In this case the client application will call the second API to validate the OTP. The user will be signed on only after successful OTP validation. This flow should be used when the user account is created by user himself/herself or the user is present to provide the OTP. If this parameter is ‘N’, the user account will be created without OTP validation. The OTP validation will be performed when the user signs in for the first time in DigiLocker. This flow should be used when the user account needs to be created in the absence of the user.
    :type verification: str

    """
    return web.Response(status=200)


async def verify_otp_id(request: web.Request, clientid=None, hmac=None, mobile=None, otp=None, ts=None) -> web.Response:
    """Verify OTP

    This API is used to verify the OTP sent by DigiLocker during the sign up API call above.

    :param clientid: Provide the client id that was created during the application registration process on Partners Portal.
    :type clientid: str
    :param hmac: Provide SHA-256 encrypted value of the client secret, clientid and ts parameters above concatenated in this sequence (client secret, clientid, ts). The hmac parameter is used by DigiLocker to ensure the data integrity and authentication of the request. Use the Client Secret Key generated during the application registration process on Partners Portal as the client secret.
    :type hmac: str
    :param mobile: This is the mobile number of the user. DigiLocker will check whether an account exists for this mobile number. Either uid or mobile is required to verify whether an account exists.
    :type mobile: int
    :param otp: The OTP provided by the user.
    :type otp: int
    :param ts: Provide a timestamp value in UNIX (or POSIX) format in IST time zone in seconds. This timestamp value must not be older than 30 minutes.
    :type ts: str

    """
    return web.Response(status=200)

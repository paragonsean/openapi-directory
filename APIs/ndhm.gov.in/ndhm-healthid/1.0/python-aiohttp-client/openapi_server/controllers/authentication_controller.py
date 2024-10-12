from typing import List, Dict
from aiohttp import web

from openapi_server.models.auth_account_aadhaar_bio_request import AuthAccountAadhaarBioRequest
from openapi_server.models.auth_account_aadhaar_otp_request import AuthAccountAadhaarOTPRequest
from openapi_server.models.auth_account_mobile_otp_request import AuthAccountMobileOTPRequest
from openapi_server.models.auth_account_with_demographics_request import AuthAccountWithDemographicsRequest
from openapi_server.models.auth_init_request import AuthInitRequest
from openapi_server.models.auth_mobile_otp_request import AuthMobileOTPRequest
from openapi_server.models.auth_with_mobile_txn_and_user_data import AuthWithMobileTxnAndUserData
from openapi_server.models.auth_with_password_request import AuthWithPasswordRequest
from openapi_server.models.jwt_request import JwtRequest
from openapi_server.models.jwt_response import JwtResponse
from openapi_server.models.resend_otp_request import ResendOTPRequest
from openapi_server.models.txn_response import TxnResponse
from openapi_server import util


async def auth_account_password_request_using_post(request: web.Request, authentication_request, accept_language=None) -> web.Response:
    """Authentication with PASSWORD based auth transaction.

    

    :param authentication_request: authenticationRequest
    :type authentication_request: dict | bytes
    :param accept_language: 
    :type accept_language: str

    """
    authentication_request = AuthWithPasswordRequest.from_dict(authentication_request)
    return web.Response(status=200)


async def auth_with_mobile_token_using_post(request: web.Request, auth_request, accept_language=None) -> web.Response:
    """Authenticate using verified Mobile Number and user data

    

    :param auth_request: authRequest
    :type auth_request: dict | bytes
    :param accept_language: 
    :type accept_language: str

    """
    auth_request = AuthWithMobileTxnAndUserData.from_dict(auth_request)
    return web.Response(status=200)


async def authenticate_user_using_post(request: web.Request, auth_request, accept_language=None) -> web.Response:
    """Authenticate request to generate Mobile OTP using Health ID number / Health ID

    

    :param auth_request: authRequest
    :type auth_request: dict | bytes
    :param accept_language: 
    :type accept_language: str

    """
    auth_request = AuthMobileOTPRequest.from_dict(auth_request)
    return web.Response(status=200)


async def authenticate_with_password_using_post(request: web.Request, authentication_request, accept_language=None) -> web.Response:
    """Authenticate using Health ID number / Health ID and password

    

    :param authentication_request: authenticationRequest
    :type authentication_request: dict | bytes
    :param accept_language: 
    :type accept_language: str

    """
    authentication_request = JwtRequest.from_dict(authentication_request)
    return web.Response(status=200)


async def cert_using_get(request: web.Request, accept_language=None) -> web.Response:
    """Auth token public key.

    

    :param accept_language: 
    :type accept_language: str

    """
    return web.Response(status=200)


async def confirm_with_aadhaar_bio_using_post(request: web.Request, authentication_request, accept_language=None) -> web.Response:
    """Authentication with Aadhaar Biometric based auth transaction.

    

    :param authentication_request: authenticationRequest
    :type authentication_request: dict | bytes
    :param accept_language: 
    :type accept_language: str

    """
    authentication_request = AuthAccountAadhaarBioRequest.from_dict(authentication_request)
    return web.Response(status=200)


async def confirm_with_aadhaar_otp_using_post(request: web.Request, authentication_request, accept_language=None) -> web.Response:
    """Authentication with Aadhaar OTP based auth transaction.

    

    :param authentication_request: authenticationRequest
    :type authentication_request: dict | bytes
    :param accept_language: 
    :type accept_language: str

    """
    authentication_request = AuthAccountAadhaarOTPRequest.from_dict(authentication_request)
    return web.Response(status=200)


async def confirm_with_demographics_using_post(request: web.Request, authentication_request, accept_language=None) -> web.Response:
    """Authenticate using demographic data of user.

    

    :param authentication_request: authenticationRequest
    :type authentication_request: dict | bytes
    :param accept_language: 
    :type accept_language: str

    """
    authentication_request = AuthAccountWithDemographicsRequest.from_dict(authentication_request)
    return web.Response(status=200)


async def confirm_with_mobile_using_post(request: web.Request, authentication_request, accept_language=None) -> web.Response:
    """Authentication with Mobile OTP based auth transaction.

    

    :param authentication_request: authenticationRequest
    :type authentication_request: dict | bytes
    :param accept_language: 
    :type accept_language: str

    """
    authentication_request = AuthAccountMobileOTPRequest.from_dict(authentication_request)
    return web.Response(status=200)


async def initiate_auth_using_post(request: web.Request, auth_request, accept_language=None) -> web.Response:
    """Initiate authentication process for given Health ID

    

    :param auth_request: authRequest
    :type auth_request: dict | bytes
    :param accept_language: 
    :type accept_language: str

    """
    auth_request = AuthInitRequest.from_dict(auth_request)
    return web.Response(status=200)


async def resend_auth_mobile_otp_using_post(request: web.Request, resend_otp_request, accept_language=None) -> web.Response:
    """Resend Aadhaar/Mobile OTP for Authentication Transaction.

    

    :param resend_otp_request: resendOtpRequest
    :type resend_otp_request: dict | bytes
    :param accept_language: 
    :type accept_language: str

    """
    resend_otp_request = ResendOTPRequest.from_dict(resend_otp_request)
    return web.Response(status=200)

from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_account_by_verified_mobile_request import CreateAccountByVerifiedMobileRequest
from openapi_server.models.create_account_jwt_response import CreateAccountJwtResponse
from openapi_server.models.generate_mobile_otp_request import GenerateMobileOTPRequest
from openapi_server.models.mobile_verification_token import MobileVerificationToken
from openapi_server.models.resend_otp_request import ResendOTPRequest
from openapi_server.models.txn_response import TxnResponse
from openapi_server.models.verify_mobile_request import VerifyMobileRequest
from openapi_server import util


async def generate_mobile_otp_using_post1(request: web.Request, generate_otp_request, accept_language=None) -> web.Response:
    """Generate Mobile OTP to start registration

    Generate Mobile OTP to start registration transaction.

    :param generate_otp_request: generateOtpRequest
    :type generate_otp_request: dict | bytes
    :param accept_language: 
    :type accept_language: str

    """
    generate_otp_request = GenerateMobileOTPRequest.from_dict(generate_otp_request)
    return web.Response(status=200)


async def resent_otp_using_post(request: web.Request, resend_request, accept_language=None) -> web.Response:
    """Resend Mobile OTP for Health ID registration

    Resend Mobile OTP in an existing transaction in case previous OTP is not received.

    :param resend_request: resendRequest
    :type resend_request: dict | bytes
    :param accept_language: 
    :type accept_language: str

    """
    resend_request = ResendOTPRequest.from_dict(resend_request)
    return web.Response(status=200)


async def verify_mobile_otp_using_post(request: web.Request, verify_otp_request, accept_language=None) -> web.Response:
    """Verify Mobile OTP sent as part of registration transaction.

    Verify Mobile OTP in current registration transaction.

    :param verify_otp_request: verifyOtpRequest
    :type verify_otp_request: dict | bytes
    :param accept_language: 
    :type accept_language: str

    """
    verify_otp_request = VerifyMobileRequest.from_dict(verify_otp_request)
    return web.Response(status=200)


async def verify_user_via_mobile_using_post(request: web.Request, create_account_request, accept_language=None) -> web.Response:
    """Create Health ID with verified mobile token

    

    :param create_account_request: createAccountRequest
    :type create_account_request: dict | bytes
    :param accept_language: 
    :type accept_language: str

    """
    create_account_request = CreateAccountByVerifiedMobileRequest.from_dict(create_account_request)
    return web.Response(status=200)

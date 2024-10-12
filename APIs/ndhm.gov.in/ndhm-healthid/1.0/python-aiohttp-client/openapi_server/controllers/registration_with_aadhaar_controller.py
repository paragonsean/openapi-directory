from typing import List, Dict
from aiohttp import web

from openapi_server.models.aadhar_number_request_payload import AadharNumberRequestPayload
from openapi_server.models.aadhar_otp_generate_request_pay_load import AadharOtpGenerateRequestPayLoad
from openapi_server.models.create_account_jwt_response import CreateAccountJwtResponse
from openapi_server.models.create_account_with_aadhaar_otp import CreateAccountWithAadhaarOtp
from openapi_server.models.create_account_with_pre_verified_aadhaar import CreateAccountWithPreVerifiedAadhaar
from openapi_server.models.generate_mobile_otp_for_txn_request import GenerateMobileOTPForTxnRequest
from openapi_server.models.resend_otp_request import ResendOTPRequest
from openapi_server.models.txn_response import TxnResponse
from openapi_server.models.verify_aadhaar_otp import VerifyAadhaarOtp
from openapi_server.models.verify_aadhaar_with_bio import VerifyAadhaarWithBio
from openapi_server.models.verify_mobile_request import VerifyMobileRequest
from openapi_server import util


async def create_aadhaar_account_using_post(request: web.Request, account_request, accept_language=None) -> web.Response:
    """Create Health ID using pre-verified Aadhaar &amp; Mobile.

    Create Health ID using pre-verified Aadhaar &amp; Mobile.

    :param account_request: accountRequest
    :type account_request: dict | bytes
    :param accept_language: 
    :type accept_language: str

    """
    account_request = CreateAccountWithPreVerifiedAadhaar.from_dict(account_request)
    return web.Response(status=200)


async def generate_aadhar_otp_using_post(request: web.Request, generate_otp_request, accept_language=None) -> web.Response:
    """Generate Aadhaar OTP on registrered mobile number

    Generate Aadhaar OTP on registrered mobile number

    :param generate_otp_request: generateOtpRequest
    :type generate_otp_request: dict | bytes
    :param accept_language: 
    :type accept_language: str

    """
    generate_otp_request = AadharOtpGenerateRequestPayLoad.from_dict(generate_otp_request)
    return web.Response(status=200)


async def generate_mobile_otp_for_txn_using_post(request: web.Request, request, accept_language=None) -> web.Response:
    """Generate Mobile OTP for verification.

    Generate Mobile OTP to verify mobile number.

    :param request: request
    :type request: dict | bytes
    :param accept_language: 
    :type accept_language: str

    """
    request = GenerateMobileOTPForTxnRequest.from_dict(request)
    return web.Response(status=200)


async def get_health_id_numbers_by_aadhar_using_post(request: web.Request, aadhar_number_request_payload, accept_language=None) -> web.Response:
    """Search health id number using aadhar.

    Search health id number using aadhar.

    :param aadhar_number_request_payload: aadharNumberRequestPayload
    :type aadhar_number_request_payload: dict | bytes
    :param accept_language: 
    :type accept_language: str

    """
    aadhar_number_request_payload = AadharNumberRequestPayload.from_dict(aadhar_number_request_payload)
    return web.Response(status=200)


async def resend_aadhar_otp_using_post(request: web.Request, request, accept_language=None) -> web.Response:
    """Resend Aadhaar OTP on registrered mobile number to create Health ID.

    Resend Aadhar OTP on registrered mobile number

    :param request: request
    :type request: dict | bytes
    :param accept_language: 
    :type accept_language: str

    """
    request = ResendOTPRequest.from_dict(request)
    return web.Response(status=200)


async def verify_aadhar_bio_using_post(request: web.Request, verify_aadhar_otp_request, accept_language=None) -> web.Response:
    """Verify Aadhaar using biometrics.

    Verify Aadhaar using biometrics

    :param verify_aadhar_otp_request: verifyAadharOtpRequest
    :type verify_aadhar_otp_request: dict | bytes
    :param accept_language: 
    :type accept_language: str

    """
    verify_aadhar_otp_request = VerifyAadhaarWithBio.from_dict(verify_aadhar_otp_request)
    return web.Response(status=200)


async def verify_aadhar_otp_only_using_post(request: web.Request, verify_aadhaar_otp, accept_language=None) -> web.Response:
    """Verify Aadhaar OTP and continue for mobile verification.

    Verify Aadhaar OTP received on registrered mobile number

    :param verify_aadhaar_otp: verifyAadhaarOtp
    :type verify_aadhaar_otp: dict | bytes
    :param accept_language: 
    :type accept_language: str

    """
    verify_aadhaar_otp = VerifyAadhaarOtp.from_dict(verify_aadhaar_otp)
    return web.Response(status=200)


async def verify_aadhar_otp_using_post_0(request: web.Request, verify_aadhar_otp_request, accept_language=None) -> web.Response:
    """Verify Aadhaar OTP on registrered mobile number to create Health ID.

    Verify Aadhar OTP received on registrered mobile number

    :param verify_aadhar_otp_request: verifyAadharOtpRequest
    :type verify_aadhar_otp_request: dict | bytes
    :param accept_language: 
    :type accept_language: str

    """
    verify_aadhar_otp_request = CreateAccountWithAadhaarOtp.from_dict(verify_aadhar_otp_request)
    return web.Response(status=200)


async def verify_mobile_otp_for_txn_using_post(request: web.Request, request, accept_language=None) -> web.Response:
    """Verify Mobile OTP in an existing transaction.

    Verify Mobile OTP in an existing transaction.

    :param request: request
    :type request: dict | bytes
    :param accept_language: 
    :type accept_language: str

    """
    request = VerifyMobileRequest.from_dict(request)
    return web.Response(status=200)

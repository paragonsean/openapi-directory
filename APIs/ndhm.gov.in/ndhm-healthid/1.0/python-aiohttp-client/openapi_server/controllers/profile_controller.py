from typing import List, Dict
from aiohttp import web

from openapi_server.models.hid_change_password_request_payload import HidChangePasswordRequestPayload
from openapi_server.models.hid_otp_request_paylaod import HidOtpRequestPaylaod
from openapi_server.models.txn_response import TxnResponse
from openapi_server.models.update_account_request import UpdateAccountRequest
from openapi_server.models.user_dto import UserDTO
from openapi_server.models.validate_token_request import ValidateTokenRequest
from openapi_server.models.verify_aadhaar_otp import VerifyAadhaarOtp
from openapi_server import util


async def change_password_via_aadhar_using_post(request: web.Request, x_token, hid_otp_request_paylaod, accept_language=None) -> web.Response:
    """Change password via Aadhar for heath id.

    Change password via Aadhar for heath id.

    :param x_token: Auth Token
    :type x_token: str
    :param hid_otp_request_paylaod: hidOtpRequestPaylaod
    :type hid_otp_request_paylaod: dict | bytes
    :param accept_language: 
    :type accept_language: str

    """
    hid_otp_request_paylaod = HidOtpRequestPaylaod.from_dict(hid_otp_request_paylaod)
    return web.Response(status=200)


async def change_password_via_mobile_using_post(request: web.Request, x_token, hid_otp_request_paylaod, accept_language=None) -> web.Response:
    """Change password via mobile for heath id.

    Change password via mobile for heath id.

    :param x_token: Auth Token
    :type x_token: str
    :param hid_otp_request_paylaod: hidOtpRequestPaylaod
    :type hid_otp_request_paylaod: dict | bytes
    :param accept_language: 
    :type accept_language: str

    """
    hid_otp_request_paylaod = HidOtpRequestPaylaod.from_dict(hid_otp_request_paylaod)
    return web.Response(status=200)


async def change_password_via_using_post(request: web.Request, x_token, health_facility_password_request, accept_language=None) -> web.Response:
    """Change password via password for heath id.

    Change password via password for heath id.

    :param x_token: Auth Token
    :type x_token: str
    :param health_facility_password_request: healthFacilityPasswordRequest
    :type health_facility_password_request: dict | bytes
    :param accept_language: 
    :type accept_language: str

    """
    health_facility_password_request = HidChangePasswordRequestPayload.from_dict(health_facility_password_request)
    return web.Response(status=200)


async def delete_account_using_delete(request: web.Request, x_token, accept_language=None) -> web.Response:
    """Delete account

    

    :param x_token: Auth Token
    :type x_token: str
    :param accept_language: 
    :type accept_language: str

    """
    return web.Response(status=200)


async def generate_aadhar_otp_using_get(request: web.Request, x_token, accept_language=None) -> web.Response:
    """Generate Aadhaar OTP on registrered mobile number.

    Generate Aadhaar OTP on registrered mobile number.

    :param x_token: Auth Token
    :type x_token: str
    :param accept_language: 
    :type accept_language: str

    """
    return web.Response(status=200)


async def generate_card_using_get(request: web.Request, x_token, accept_language=None) -> web.Response:
    """Generate Health ID card in PDF format

    

    :param x_token: Auth Token
    :type x_token: str
    :param accept_language: 
    :type accept_language: str

    """
    return web.Response(status=200)


async def generate_mobile_otp_using_get(request: web.Request, x_token, accept_language=None) -> web.Response:
    """Generate Mobile OTP to start registration.

    Generate Mobile OTP to start registration.

    :param x_token: Auth Token
    :type x_token: str
    :param accept_language: 
    :type accept_language: str

    """
    return web.Response(status=200)


async def generate_png_card_using_get(request: web.Request, x_token, accept_language=None) -> web.Response:
    """Generate Health ID card PNG

    

    :param x_token: Auth Token
    :type x_token: str
    :param accept_language: 
    :type accept_language: str

    """
    return web.Response(status=200)


async def generate_svg_card_using_get(request: web.Request, x_token, accept_language=None) -> web.Response:
    """Generate Health ID card SVG

    

    :param x_token: Auth Token
    :type x_token: str
    :param accept_language: 
    :type accept_language: str

    """
    return web.Response(status=200)


async def generatere_kyc_aadhar_otp_using_post(request: web.Request, x_token, accept_language=None) -> web.Response:
    """Generate Aadhaar OTP on registrered for link account with aadhar number

    Generate Aadhaar OTP on registrered for link account with aadhar number

    :param x_token: Auth Token
    :type x_token: str
    :param accept_language: 
    :type accept_language: str

    """
    return web.Response(status=200)


async def get_account_information_using_get(request: web.Request, x_token, accept_language=None) -> web.Response:
    """Get account information.

    

    :param x_token: Auth Token
    :type x_token: str
    :param accept_language: 
    :type accept_language: str

    """
    return web.Response(status=200)


async def get_benefits_using_get(request: web.Request, x_token, accept_language=None) -> web.Response:
    """Get List of Benefits associated with HealthID.

    

    :param x_token: Auth Token
    :type x_token: str
    :param accept_language: 
    :type accept_language: str

    """
    return web.Response(status=200)


async def get_qr_code_using_get(request: web.Request, x_token, accept_language=None) -> web.Response:
    """Get Quick Response code in PNG format for this account.

    

    :param x_token: Auth Token
    :type x_token: str
    :param accept_language: 
    :type accept_language: str

    """
    return web.Response(status=200)


async def update_account_information_using_post(request: web.Request, x_token, request, accept_language=None) -> web.Response:
    """Update account information

    

    :param x_token: Auth Token
    :type x_token: str
    :param request: request
    :type request: dict | bytes
    :param accept_language: 
    :type accept_language: str

    """
    request = UpdateAccountRequest.from_dict(request)
    return web.Response(status=200)


async def validate_token_using_post(request: web.Request, request, accept_language=None) -> web.Response:
    """Validate auth token

    

    :param request: request
    :type request: dict | bytes
    :param accept_language: 
    :type accept_language: str

    """
    request = ValidateTokenRequest.from_dict(request)
    return web.Response(status=200)


async def verify_aadhar_otp_only_using_post1(request: web.Request, x_token, verify_aadhaar_otp, accept_language=None) -> web.Response:
    """Verify Aadhaar OTP to complete KYC/re-KYC verification.

    Verify Aadhaar OTP to complete KYC/re-KYC verification

    :param x_token: Auth Token
    :type x_token: str
    :param verify_aadhaar_otp: verifyAadhaarOtp
    :type verify_aadhaar_otp: dict | bytes
    :param accept_language: 
    :type accept_language: str

    """
    verify_aadhaar_otp = VerifyAadhaarOtp.from_dict(verify_aadhaar_otp)
    return web.Response(status=200)

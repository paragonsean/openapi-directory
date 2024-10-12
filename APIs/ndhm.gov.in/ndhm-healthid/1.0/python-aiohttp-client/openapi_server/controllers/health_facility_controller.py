from typing import List, Dict
from aiohttp import web

from openapi_server.models.aadhar_otp_generate_request_pay_load import AadharOtpGenerateRequestPayLoad
from openapi_server.models.create_account_jwt_response import CreateAccountJwtResponse
from openapi_server.models.create_account_with_pre_verified_aadhaar import CreateAccountWithPreVerifiedAadhaar
from openapi_server.models.health_facility_authentication_request import HealthFacilityAuthenticationRequest
from openapi_server.models.health_facility_changed_password_request import HealthFacilityChangedPasswordRequest
from openapi_server.models.health_facility_password_request import HealthFacilityPasswordRequest
from openapi_server.models.txn_response import TxnResponse
from openapi_server import util


async def authenticate_health_facility_using_post(request: web.Request, health_facility_authentication_request, accept_language=None) -> web.Response:
    """Generate token for heath facility id.

    Generate token for heath facility id.

    :param health_facility_authentication_request: healthFacilityAuthenticationRequest
    :type health_facility_authentication_request: dict | bytes
    :param accept_language: 
    :type accept_language: str

    """
    health_facility_authentication_request = HealthFacilityAuthenticationRequest.from_dict(health_facility_authentication_request)
    return web.Response(status=200)


async def change_password_using_post(request: web.Request, health_facility_password_request, accept_language=None) -> web.Response:
    """Change password for heath facility id.

    Change password for heath facility id.

    :param health_facility_password_request: healthFacilityPasswordRequest
    :type health_facility_password_request: dict | bytes
    :param accept_language: 
    :type accept_language: str

    """
    health_facility_password_request = HealthFacilityChangedPasswordRequest.from_dict(health_facility_password_request)
    return web.Response(status=200)


async def create_aadhaar_account_using_post1(request: web.Request, account_request, accept_language=None) -> web.Response:
    """Generate Health ID card SVG

    

    :param account_request: accountRequest
    :type account_request: dict | bytes
    :param accept_language: 
    :type accept_language: str

    """
    account_request = CreateAccountWithPreVerifiedAadhaar.from_dict(account_request)
    return web.Response(status=200)


async def generate_facility_otp_using_post(request: web.Request, x_token, generate_otp_request, accept_language=None) -> web.Response:
    """Generate health hacility OTP on registrered mobile number

    Generate health facility OTP on registrered mobile number

    :param x_token: Auth Token
    :type x_token: str
    :param generate_otp_request: generateOtpRequest
    :type generate_otp_request: dict | bytes
    :param accept_language: 
    :type accept_language: str

    """
    generate_otp_request = AadharOtpGenerateRequestPayLoad.from_dict(generate_otp_request)
    return web.Response(status=200)


async def generate_password_using_post(request: web.Request, health_facility_password_request, accept_language=None) -> web.Response:
    """Generates password for heath facility id.

    Generates password for heath facility id.

    :param health_facility_password_request: healthFacilityPasswordRequest
    :type health_facility_password_request: dict | bytes
    :param accept_language: 
    :type accept_language: str

    """
    health_facility_password_request = HealthFacilityPasswordRequest.from_dict(health_facility_password_request)
    return web.Response(status=200)


async def generate_svg_card_using_get1(request: web.Request, health_id, x_token, accept_language=None) -> web.Response:
    """generateSvgCard

    

    :param health_id: Your health id
    :type health_id: str
    :param x_token: Auth Token
    :type x_token: str
    :param accept_language: 
    :type accept_language: str

    """
    return web.Response(status=200)


async def reset_password_using_post(request: web.Request, health_facility_password_request, accept_language=None) -> web.Response:
    """Reset password for heath facility id.

    Reset password for heath facility id.

    :param health_facility_password_request: healthFacilityPasswordRequest
    :type health_facility_password_request: dict | bytes
    :param accept_language: 
    :type accept_language: str

    """
    health_facility_password_request = HealthFacilityPasswordRequest.from_dict(health_facility_password_request)
    return web.Response(status=200)

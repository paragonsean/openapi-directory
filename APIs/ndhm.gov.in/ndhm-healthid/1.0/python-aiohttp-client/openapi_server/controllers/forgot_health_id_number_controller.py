from typing import List, Dict
from aiohttp import web

from openapi_server.models.aadhar_otp_generate_request_pay_load import AadharOtpGenerateRequestPayLoad
from openapi_server.models.auth_account_aadhaar_otp_request import AuthAccountAadhaarOTPRequest
from openapi_server.models.generate_mobile_otp_request import GenerateMobileOTPRequest
from openapi_server.models.retrieve_health_id_payload_response import RetrieveHealthIdPayloadResponse
from openapi_server.models.retrive_health_id_mobile_pay_load import RetriveHealthIdMobilePayLoad
from openapi_server.models.txn_response import TxnResponse
from openapi_server import util


async def generate_aadhar_otp_using_post1(request: web.Request, generate_otp_request, accept_language=None) -> web.Response:
    """Generate Aadhaar OTP on registrered mobile number

    Generate Aadhaar OTP on registrered mobile number

    :param generate_otp_request: generateOtpRequest
    :type generate_otp_request: dict | bytes
    :param accept_language: 
    :type accept_language: str

    """
    generate_otp_request = AadharOtpGenerateRequestPayLoad.from_dict(generate_otp_request)
    return web.Response(status=200)


async def generate_mobile_otp_using_post(request: web.Request, generate_otp_request, accept_language=None) -> web.Response:
    """Generate Mobile OTP to start registration

    Generate Mobile OTP to start registration transaction.

    :param generate_otp_request: generateOtpRequest
    :type generate_otp_request: dict | bytes
    :param accept_language: 
    :type accept_language: str

    """
    generate_otp_request = GenerateMobileOTPRequest.from_dict(generate_otp_request)
    return web.Response(status=200)


async def retrieval_health_id_by_aadhar_using_post(request: web.Request, auth_account_aadhaar_otp_request, accept_language=None) -> web.Response:
    """Verify aadhar OTP sent as part of forgetHealth id.

    Verify aadhar OTP sent as part of forgetHealth id.

    :param auth_account_aadhaar_otp_request: authAccountAadhaarOTPRequest
    :type auth_account_aadhaar_otp_request: dict | bytes
    :param accept_language: 
    :type accept_language: str

    """
    auth_account_aadhaar_otp_request = AuthAccountAadhaarOTPRequest.from_dict(auth_account_aadhaar_otp_request)
    return web.Response(status=200)


async def retrieval_health_id_by_mobile_using_post(request: web.Request, retrive_health_id_mobile_pay_load, accept_language=None) -> web.Response:
    """Verify Mobile OTP sent as  part of forgetHealth id.

    Verify Mobile OTP sent as  part of forgetHealth id.

    :param retrive_health_id_mobile_pay_load: retriveHealthIdMobilePayLoad
    :type retrive_health_id_mobile_pay_load: dict | bytes
    :param accept_language: 
    :type accept_language: str

    """
    retrive_health_id_mobile_pay_load = RetriveHealthIdMobilePayLoad.from_dict(retrive_health_id_mobile_pay_load)
    return web.Response(status=200)

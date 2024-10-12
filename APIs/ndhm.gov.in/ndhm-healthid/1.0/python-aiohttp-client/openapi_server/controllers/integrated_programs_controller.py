from typing import List, Dict
from aiohttp import web

from openapi_server.models.aadhar_number_request_payload import AadharNumberRequestPayload
from openapi_server.models.aadhar_otp_generate_request_pay_load import AadharOtpGenerateRequestPayLoad
from openapi_server.models.create_hid_demo_auth_request import CreateHIdDemoAuthRequest
from openapi_server.models.create_health_id_opt_request import CreateHealthIdOptRequest
from openapi_server.models.create_hid_biometric_request import CreateHidBiometricRequest
from openapi_server.models.create_hid_mobile_request import CreateHidMobileRequest
from openapi_server.models.create_hid_notify_benefit_request import CreateHidNotifyBenefitRequest
from openapi_server.models.generate_mobile_otp_request import GenerateMobileOTPRequest
from openapi_server.models.hid_benefit_delink_request_payload import HidBenefitDelinkRequestPayload
from openapi_server.models.hid_benefit_linked_request_payload import HidBenefitLinkedRequestPayload
from openapi_server.models.hid_benefit_linked_response_payload import HidBenefitLinkedResponsePayload
from openapi_server.models.hid_benefit_name_search_request import HidBenefitNameSearchRequest
from openapi_server.models.hid_benefit_request_payload import HidBenefitRequestPayload
from openapi_server.models.hid_benefit_search_response_payload import HidBenefitSearchResponsePayload
from openapi_server.models.hid_status_request_payload import HidStatusRequestPayload
from openapi_server.models.hid_update_account_request import HidUpdateAccountRequest
from openapi_server.models.hid_update_mobilet_request import HidUpdateMobiletRequest
from openapi_server.models.txn_response import TxnResponse
from openapi_server.models.user_dto import UserDTO
from openapi_server import util


async def create_health_id_by_demo_auth_using_post(request: web.Request, create_hid_demo_auth_request, accept_language=None) -> web.Response:
    """Create health id using Aadhaar Demo Auth.

    Create health id using Aadhaar Demo Auth.

    :param create_hid_demo_auth_request: createHIdDemoAuthRequest
    :type create_hid_demo_auth_request: dict | bytes
    :param accept_language: 
    :type accept_language: str

    """
    create_hid_demo_auth_request = CreateHIdDemoAuthRequest.from_dict(create_hid_demo_auth_request)
    return web.Response(status=200)


async def create_health_id_by_mobile_using_post(request: web.Request, create_hid_mobile_request, accept_language=None) -> web.Response:
    """Create health id using mobile Authentication.

    Create health id using mobile Authentication.

    :param create_hid_mobile_request: createHidMobileRequest
    :type create_hid_mobile_request: dict | bytes
    :param accept_language: 
    :type accept_language: str

    """
    create_hid_mobile_request = CreateHidMobileRequest.from_dict(create_hid_mobile_request)
    return web.Response(status=200)


async def delink_hid_benefit_using_post(request: web.Request, hid_benefit_linked_request_payload, accept_language=None) -> web.Response:
    """De-Linked with hid.

    De-Linked with hid.

    :param hid_benefit_linked_request_payload: hidBenefitLinkedRequestPayload
    :type hid_benefit_linked_request_payload: dict | bytes
    :param accept_language: 
    :type accept_language: str

    """
    hid_benefit_linked_request_payload = HidBenefitDelinkRequestPayload.from_dict(hid_benefit_linked_request_payload)
    return web.Response(status=200)


async def find_by_aadhar_using_post(request: web.Request, aadhar_number_request_payload, accept_language=None) -> web.Response:
    """Search health id number using aadhar or aadhar token.

    Search health id number using aadhar or aadhar token.

    :param aadhar_number_request_payload: aadharNumberRequestPayload
    :type aadhar_number_request_payload: dict | bytes
    :param accept_language: 
    :type accept_language: str

    """
    aadhar_number_request_payload = AadharNumberRequestPayload.from_dict(aadhar_number_request_payload)
    return web.Response(status=200)


async def find_by_health_id_using_post(request: web.Request, search_request, accept_language=None) -> web.Response:
    """Search benefit using health id number.

    Search benefit using health id number

    :param search_request: searchRequest
    :type search_request: dict | bytes
    :param accept_language: 
    :type accept_language: str

    """
    search_request = HidBenefitNameSearchRequest.from_dict(search_request)
    return web.Response(status=200)


async def generate_aadhar_otp_using_post2(request: web.Request, generate_otp_request, accept_language=None) -> web.Response:
    """Generate Aadhaar OTP on registrered mobile number

    Generate Aadhaar OTP on registrered mobile number

    :param generate_otp_request: generateOtpRequest
    :type generate_otp_request: dict | bytes
    :param accept_language: 
    :type accept_language: str

    """
    generate_otp_request = AadharOtpGenerateRequestPayLoad.from_dict(generate_otp_request)
    return web.Response(status=200)


async def generate_mobile_otp_using_post_0(request: web.Request, generate_otp_request, accept_language=None) -> web.Response:
    """Generate mobile OTP on registrered mobile number

    Generate mobile OTP on registrered mobile number

    :param generate_otp_request: generateOtpRequest
    :type generate_otp_request: dict | bytes
    :param accept_language: 
    :type accept_language: str

    """
    generate_otp_request = GenerateMobileOTPRequest.from_dict(generate_otp_request)
    return web.Response(status=200)


async def link_hid_benefit_using_post(request: web.Request, hid_benefit_linked_request_payload, accept_language=None) -> web.Response:
    """Linked with hid.

    Linked with hid.

    :param hid_benefit_linked_request_payload: hidBenefitLinkedRequestPayload
    :type hid_benefit_linked_request_payload: dict | bytes
    :param accept_language: 
    :type accept_language: str

    """
    hid_benefit_linked_request_payload = HidBenefitLinkedRequestPayload.from_dict(hid_benefit_linked_request_payload)
    return web.Response(status=200)


async def notify_benefit_using_post(request: web.Request, create_hid_notify_benefit_request, accept_language=None) -> web.Response:
    """Create health id using notify Benefit.

    Create health id using notify Benefit.

    :param create_hid_notify_benefit_request: createHidNotifyBenefitRequest
    :type create_hid_notify_benefit_request: dict | bytes
    :param accept_language: 
    :type accept_language: str

    """
    create_hid_notify_benefit_request = CreateHidNotifyBenefitRequest.from_dict(create_hid_notify_benefit_request)
    return web.Response(status=200)


async def update_account_information_using_post1(request: web.Request, request, accept_language=None) -> web.Response:
    """Update account information

    

    :param request: request
    :type request: dict | bytes
    :param accept_language: 
    :type accept_language: str

    """
    request = HidUpdateAccountRequest.from_dict(request)
    return web.Response(status=200)


async def update_mobile_information_using_post(request: web.Request, request, accept_language=None) -> web.Response:
    """Update mobile number for account.

    

    :param request: request
    :type request: dict | bytes
    :param accept_language: 
    :type accept_language: str

    """
    request = HidUpdateMobiletRequest.from_dict(request)
    return web.Response(status=200)


async def update_status_using_post(request: web.Request, generate_otp_request, accept_language=None) -> web.Response:
    """Update health id status .

    Update health id status.

    :param generate_otp_request: generateOtpRequest
    :type generate_otp_request: dict | bytes
    :param accept_language: 
    :type accept_language: str

    """
    generate_otp_request = HidStatusRequestPayload.from_dict(generate_otp_request)
    return web.Response(status=200)


async def verify_aadhar_otp_using_post(request: web.Request, create_health_id_opt_request, accept_language=None) -> web.Response:
    """Create health id using Aadhaar Number Otp.

    Create health id using Aadhaar number opt

    :param create_health_id_opt_request: createHealthIdOptRequest
    :type create_health_id_opt_request: dict | bytes
    :param accept_language: 
    :type accept_language: str

    """
    create_health_id_opt_request = CreateHealthIdOptRequest.from_dict(create_health_id_opt_request)
    return web.Response(status=200)


async def verify_bio_using_post(request: web.Request, create_hid_biometric_request, accept_language=None) -> web.Response:
    """Create health id using Biometric Authentication.

    Create health id using Biometric Authentication.

    :param create_hid_biometric_request: createHidBiometricRequest
    :type create_hid_biometric_request: dict | bytes
    :param accept_language: 
    :type accept_language: str

    """
    create_hid_biometric_request = CreateHidBiometricRequest.from_dict(create_hid_biometric_request)
    return web.Response(status=200)

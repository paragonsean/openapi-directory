from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.patient_auth_confirm_request import PatientAuthConfirmRequest
from openapi_server.models.patient_auth_init_request import PatientAuthInitRequest
from openapi_server.models.patient_auth_mode_query_request import PatientAuthModeQueryRequest
from openapi_server.models.patient_auth_notification_acknowledgement import PatientAuthNotificationAcknowledgement
from openapi_server import util


async def v05_users_auth_confirm_post(request: web.Request, authorization, body) -> web.Response:
    """Confirmation request sending token, otp or other authentication details from HIP/HIU for confirmation

    This API is called by HIP/HIUs to confirm authentication of users. The transactionId returned by the previous callback API /users/auth/on-init must be sent. If Authentication is successful the callback API will send an \&quot;access token\&quot; for subsequent purpose specific API calls. Note only **credential.authCode** or **credential.demographic** should be sent   1. demographic details are only required for  demographic auth as of now.    2. demographic details are required only in MEDIATED cases and if the **auth.mode** so demands. e.g. if **auth.mode** is DEMOGRAPHICS. Usually for demographic authentication, the name, gender and DOB must be exactly as specified in User Account.   3. demographic.identifier is optional, however maybe required if authentication so mandates.    4. credential.authCode is required for other MEDIATED authentication like MOBILE_OTP, AADHAAR_OTP.  

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatientAuthConfirmRequest.from_dict(body)
    return web.Response(status=200)


async def v05_users_auth_fetch_modes_post(request: web.Request, authorization, body) -> web.Response:
    """Get a patient&#39;s authentication modes relevant to specified purpose

    This API is meant for identify supported authentication modes for a patient given a specific purpose 

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatientAuthModeQueryRequest.from_dict(body)
    return web.Response(status=200)


async def v05_users_auth_init_post(request: web.Request, authorization, body) -> web.Response:
    """Initialize authentication from HIP

    This API is called by HIPs to initiate authentication of users. A transactionId is retuned by the corresponding callback API for confirmation of user auth. 

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatientAuthInitRequest.from_dict(body)
    return web.Response(status=200)


async def v05_users_auth_on_notify_post(request: web.Request, authorization, body) -> web.Response:
    """callback API from HIU/HIPs as acknowledgement of auth notification (in case of DIRECT auth)

    This API is called by HIU/HIPs to confirm acknowledgement for receipt of auth notification is case of DIRECT authentication.  

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatientAuthNotificationAcknowledgement.from_dict(body)
    return web.Response(status=200)

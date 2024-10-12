from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.link_confirmation_request import LinkConfirmationRequest
from openapi_server.models.patient_care_context_link_response import PatientCareContextLinkResponse
from openapi_server.models.patient_link_reference_request import PatientLinkReferenceRequest
from openapi_server import util


async def v05_links_link_confirm_post(request: web.Request, authorization, x_hip_id, body) -> web.Response:
    """Token submission by Consent Manager for link confirmation

    API to submit the token that was sent by HIP during the link request.  

    :param authorization: Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
    :type authorization: str
    :param x_hip_id: Identifier of the health information provider to which the request was intended.
    :type x_hip_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = LinkConfirmationRequest.from_dict(body)
    return web.Response(status=200)


async def v05_links_link_init_post(request: web.Request, authorization, x_hip_id, body) -> web.Response:
    """Link patient&#39;s care contexts

    Request from Gateway to links care contexts associated with only one patient   1. **Validate account reference number and care context reference number**   2. **Validate transactionId in the request with discovery request entry to check whether there was a discovery       and were these care contexts discovered or not for a given patient**   3. **Before eventual link confirmation, HIP needs to authenticate the request with the patient(eg: OTP verification)**   4. **HIP should communicate the mode of authentication of a successful request to Consent Manager** 

    :param authorization: Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
    :type authorization: str
    :param x_hip_id: Identifier of the health information provider to which the request was intended.
    :type x_hip_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatientLinkReferenceRequest.from_dict(body)
    return web.Response(status=200)


async def v05_links_link_on_add_contexts_post(request: web.Request, authorization, x_hip_id, body) -> web.Response:
    """callback API for HIP initiated patient linking /link/add-context

    If the accessToken is valid for purpose of linking, and specified details provided, CM will send \&quot;acknoweldgement.status\&quot; as SUCCESS. If any error occcurred, for example invalid token, or other required patient or care-context information not provided, then \&quot;error\&quot; attribute conveys so.    1. **accessToken must be valid and must be for the purpose of linking** 

    :param authorization: Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
    :type authorization: str
    :param x_hip_id: Identifier of the health information provider to which the request was intended.
    :type x_hip_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatientCareContextLinkResponse.from_dict(body)
    return web.Response(status=200)

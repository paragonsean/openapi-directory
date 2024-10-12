from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.patient_discovery_request import PatientDiscoveryRequest
from openapi_server.models.patient_discovery_result import PatientDiscoveryResult
from openapi_server import util


async def v05_care_contexts_discover_post(request: web.Request, authorization, x_hip_id, body) -> web.Response:
    """Discover patient&#39;s accounts

    Request for patient care context discover, made by CM for a specific HIP. It is expected that HIP will subsequently return either zero or one patient record with (potentially masked) associated care contexts   1. **At least one of the verified identifier matches**   2. **Name (fuzzy), gender matches**   3. **If YoB was given, age band(+-2) matches**   4. **If unverified identifiers were given, one of them matches**   5. **If more than one patient records would be found after aforementioned steps, then patient who matches most verified and unverified identifiers would be returned.**   6. **If there would be still more than one patients (after ranking) error would be returned**   7. **Intended HIP should be able to resolve and identify results returned in the subsequent link confirmation request via the specified transactionId**   8. **Intended HIP should store the discovery results with transactionId and care contexts discovered for subsequent link initiation** 

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param x_hip_id: Identifier of the health information provider to which the request was intended.
    :type x_hip_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatientDiscoveryRequest.from_dict(body)
    return web.Response(status=200)


async def v05_care_contexts_on_discover_post(request: web.Request, authorization, x_cm_id, body) -> web.Response:
    """Response to patient&#39;s account discovery request

    Result of patient care-context discovery request at HIP end. If a matching patient found with zero or more care contexts associated, it is specified as result attribute. If the prior discovery request, resulted in errors then it is specified in the error attribute. Reasons of errors can be    1. **more than one definitive match for the given request**    2. **no verified identifer was specified** 

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param x_cm_id: Suffix of the consent manager to which the request was intended.
    :type x_cm_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatientDiscoveryResult.from_dict(body)
    return web.Response(status=200)

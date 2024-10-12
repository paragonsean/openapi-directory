from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.patient_discovery_result import PatientDiscoveryResult
from openapi_server import util


async def v05_care_contexts_on_discover_post(request: web.Request, authorization, body) -> web.Response:
    """Response to patient&#39;s account discovery request

    Result of patient care-context discovery request at HIP end. If a matching patient found with zero or more care contexts associated, it is specified as result attribute. If the prior discovery request, resulted in errors then it is specified in the error attribute. Reasons of errors can be    1. **more than one definitive match for the given request**    2. **no verified identifer was specified** 

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatientDiscoveryResult.from_dict(body)
    return web.Response(status=200)

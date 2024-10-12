from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.hip_health_information_request import HIPHealthInformationRequest
from openapi_server import util


async def v05_health_information_hip_request_post(request: web.Request, authorization, x_hip_id, body) -> web.Response:
    """Health information data request

    API called by CM to request Health information from HIP against a validated consent artefact. The transactionId is the correlation id that HIP should use use when pushing data to the **dataPushUrl**.  

    :param authorization: Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
    :type authorization: str
    :param x_hip_id: Identifier of the health information provider to which the request was intended.
    :type x_hip_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = HIPHealthInformationRequest.from_dict(body)
    return web.Response(status=200)

from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.share_profile_request import ShareProfileRequest
from openapi_server import util


async def v05_patients_profile_share_post(request: web.Request, authorization, x_hip_id, body) -> web.Response:
    """Share patient profile details

    Request for sharing patient&#39;s profile details to HIP 

    :param authorization: Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
    :type authorization: str
    :param x_hip_id: Identifier of the health information provider to which the request was intended.
    :type x_hip_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ShareProfileRequest.from_dict(body)
    return web.Response(status=200)

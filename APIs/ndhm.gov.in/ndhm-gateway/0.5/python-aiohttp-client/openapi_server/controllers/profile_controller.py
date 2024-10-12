from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.share_profile_request import ShareProfileRequest
from openapi_server.models.share_profile_result import ShareProfileResult
from openapi_server import util


async def v05_patients_profile_on_share_post(request: web.Request, authorization, x_cm_id, body) -> web.Response:
    """Response to patient&#39;s share profile request

    Result of patient share profile request at HIP end. 

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param x_cm_id: Suffix of the consent manager to which the request was intended.
    :type x_cm_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ShareProfileResult.from_dict(body)
    return web.Response(status=200)


async def v05_patients_profile_share_post(request: web.Request, authorization, x_hip_id, body) -> web.Response:
    """Share patient profile details

    Request for sharing patient&#39;s profile details to HIP 

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param x_hip_id: Identifier of the health information provider to which the request was intended.
    :type x_hip_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ShareProfileRequest.from_dict(body)
    return web.Response(status=200)

from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.share_profile_result import ShareProfileResult
from openapi_server import util


async def v05_patients_profile_on_share_post(request: web.Request, authorization, body) -> web.Response:
    """Response to patient&#39;s share profile request

    Result of patient share profile request at HIP end. 

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param body: 
    :type body: dict | bytes

    """
    body = ShareProfileResult.from_dict(body)
    return web.Response(status=200)

from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.authorization_error import AuthorizationError
from openapi_server.models.veteran_status_confirmation import VeteranStatusConfirmation
from openapi_server.models.veteran_status_request import VeteranStatusRequest
from openapi_server import util


async def get_veteran_status(request: web.Request, body) -> web.Response:
    """Get confirmation about an individual&#39;s Veteran status according to the VA

    

    :param body: 
    :type body: dict | bytes

    """
    body = VeteranStatusRequest.from_dict(body)
    return web.Response(status=200)

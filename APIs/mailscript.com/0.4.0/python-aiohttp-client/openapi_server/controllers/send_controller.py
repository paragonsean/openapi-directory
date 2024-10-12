from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.send_request import SendRequest
from openapi_server import util


async def send(request: web.Request, body) -> web.Response:
    """Send an email

    

    :param body: request body
    :type body: dict | bytes

    """
    body = SendRequest.from_dict(body)
    return web.Response(status=200)

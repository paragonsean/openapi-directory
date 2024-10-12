from typing import List, Dict
from aiohttp import web

from openapi_server.models.parse_request import ParseRequest
from openapi_server.models.parse_response import ParseResponse
from openapi_server import util


async def get_mentions(request: web.Request, body) -> web.Response:
    """Find mentions of observations in given text

    Returns list of mentions of observation found in given text.

    :param body: 
    :type body: dict | bytes

    """
    body = ParseRequest.from_dict(body)
    return web.Response(status=200)

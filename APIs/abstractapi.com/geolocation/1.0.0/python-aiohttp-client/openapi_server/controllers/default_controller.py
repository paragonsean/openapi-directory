from typing import List, Dict
from aiohttp import web

from openapi_server.models.inline_response200 import InlineResponse200
from openapi_server import util


async def v1_get(request: web.Request, api_key, ip_address=None, fields=None) -> web.Response:
    """v1_get

    Retrieve the location of an IP address

    :param api_key: 
    :type api_key: str
    :param ip_address: 
    :type ip_address: str
    :param fields: 
    :type fields: str

    """
    return web.Response(status=200)

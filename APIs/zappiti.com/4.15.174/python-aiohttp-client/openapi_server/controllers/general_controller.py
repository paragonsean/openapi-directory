from typing import List, Dict
from aiohttp import web

from openapi_server.models.connection_details_request import ConnectionDetailsRequest
from openapi_server.models.connection_details_result import ConnectionDetailsResult
from openapi_server.models.is_alive_request import IsAliveRequest
from openapi_server.models.is_alive_result import IsAliveResult
from openapi_server import util


async def connection_details_post(request: web.Request, body) -> web.Response:
    """Get user&#39;s login details

    

    :param body: 
    :type body: dict | bytes

    """
    body = ConnectionDetailsRequest.from_dict(body)
    return web.Response(status=200)


async def is_alive_post(request: web.Request, body) -> web.Response:
    """Get server status

    

    :param body: 
    :type body: dict | bytes

    """
    body = IsAliveRequest.from_dict(body)
    return web.Response(status=200)

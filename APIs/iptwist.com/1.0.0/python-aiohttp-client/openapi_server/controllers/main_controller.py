from typing import List, Dict
from aiohttp import web

from openapi_server.models.request import Request
from openapi_server.models.response import Response
from openapi_server import util


async def root_post(request: web.Request, body) -> web.Response:
    """Geolocate a given IP address

    

    :param body: IP address
    :type body: dict | bytes

    """
    body = Request.from_dict(body)
    return web.Response(status=200)

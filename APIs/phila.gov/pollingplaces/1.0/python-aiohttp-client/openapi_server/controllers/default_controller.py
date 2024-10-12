from typing import List, Dict
from aiohttp import web

from openapi_server.models.features import Features
from openapi_server import util


async def root_get(request: web.Request, ward, division, param_callback=None) -> web.Response:
    """Get Polling Places Data

    

    :param ward: Ward Number
    :type ward: int
    :param division: Division Number
    :type division: int
    :param param_callback: Optional parameter for jsonp support.
    :type param_callback: str

    """
    return web.Response(status=200)

from typing import List, Dict
from aiohttp import web

from openapi_server.models.networks_response import NetworksResponse
from openapi_server.models.radio_error_response import RadioErrorResponse
from openapi_server import util


async def get_radio_networks(request: web.Request, x_api_key, preset=None, international=None) -> web.Response:
    """Networks

    All iPlayer Radio networks - contains business logic for masterbrand and service relationships 

    :param x_api_key: API_KEY
    :type x_api_key: str
    :param preset: Returns all networks needed for iPlayer Radio responsive web navigation
    :type preset: bool
    :param international: Returns all networks available internationally
    :type international: bool

    """
    return web.Response(status=200)

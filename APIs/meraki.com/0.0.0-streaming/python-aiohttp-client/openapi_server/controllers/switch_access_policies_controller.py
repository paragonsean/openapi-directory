from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_network_access_policies(request: web.Request, network_id) -> web.Response:
    """List the access policies for this network

    List the access policies for this network. Only valid for MS networks.

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)

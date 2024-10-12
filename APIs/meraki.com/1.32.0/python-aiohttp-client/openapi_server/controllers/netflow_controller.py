from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_network_netflow_request import UpdateNetworkNetflowRequest
from openapi_server import util


async def get_network_netflow_1(request: web.Request, network_id) -> web.Response:
    """Return the NetFlow traffic reporting settings for a network

    Return the NetFlow traffic reporting settings for a network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def update_network_netflow_1(request: web.Request, network_id, body=None) -> web.Response:
    """Update the NetFlow traffic reporting settings for a network

    Update the NetFlow traffic reporting settings for a network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkNetflowRequest.from_dict(body)
    return web.Response(status=200)

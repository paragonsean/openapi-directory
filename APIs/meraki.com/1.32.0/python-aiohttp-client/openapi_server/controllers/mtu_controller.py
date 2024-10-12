from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_network_switch_mtu200_response import GetNetworkSwitchMtu200Response
from openapi_server.models.update_network_switch_mtu_request import UpdateNetworkSwitchMtuRequest
from openapi_server import util


async def get_network_switch_mtu_1(request: web.Request, network_id) -> web.Response:
    """Return the MTU configuration

    Return the MTU configuration

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def update_network_switch_mtu_1(request: web.Request, network_id, body=None) -> web.Response:
    """Update the MTU configuration

    Update the MTU configuration

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSwitchMtuRequest.from_dict(body)
    return web.Response(status=200)

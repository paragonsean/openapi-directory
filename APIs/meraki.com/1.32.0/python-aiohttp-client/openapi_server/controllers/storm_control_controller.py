from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_network_switch_storm_control200_response import GetNetworkSwitchStormControl200Response
from openapi_server.models.update_network_switch_storm_control_request import UpdateNetworkSwitchStormControlRequest
from openapi_server import util


async def get_network_switch_storm_control_1(request: web.Request, network_id) -> web.Response:
    """Return the storm control configuration for a switch network

    Return the storm control configuration for a switch network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def update_network_switch_storm_control_1(request: web.Request, network_id, body=None) -> web.Response:
    """Update the storm control configuration for a switch network

    Update the storm control configuration for a switch network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSwitchStormControlRequest.from_dict(body)
    return web.Response(status=200)

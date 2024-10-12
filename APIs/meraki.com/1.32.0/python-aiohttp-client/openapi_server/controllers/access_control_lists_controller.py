from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_network_switch_access_control_lists200_response import GetNetworkSwitchAccessControlLists200Response
from openapi_server.models.update_network_switch_access_control_lists_request import UpdateNetworkSwitchAccessControlListsRequest
from openapi_server import util


async def get_network_switch_access_control_lists_1(request: web.Request, network_id) -> web.Response:
    """Return the access control lists for a MS network

    Return the access control lists for a MS network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def update_network_switch_access_control_lists_1(request: web.Request, network_id, body) -> web.Response:
    """Update the access control lists for a MS network

    Update the access control lists for a MS network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSwitchAccessControlListsRequest.from_dict(body)
    return web.Response(status=200)

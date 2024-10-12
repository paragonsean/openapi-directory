from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_network_appliance_single_lan200_response import GetNetworkApplianceSingleLan200Response
from openapi_server.models.update_network_appliance_single_lan_request import UpdateNetworkApplianceSingleLanRequest
from openapi_server import util


async def get_network_appliance_single_lan_1(request: web.Request, network_id) -> web.Response:
    """Return single LAN configuration

    Return single LAN configuration

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def update_network_appliance_single_lan_1(request: web.Request, network_id, body=None) -> web.Response:
    """Update single LAN configuration

    Update single LAN configuration

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceSingleLanRequest.from_dict(body)
    return web.Response(status=200)

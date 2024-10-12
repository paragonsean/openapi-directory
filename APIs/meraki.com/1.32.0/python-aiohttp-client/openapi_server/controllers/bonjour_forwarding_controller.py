from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_network_wireless_ssid_bonjour_forwarding_request import UpdateNetworkWirelessSsidBonjourForwardingRequest
from openapi_server import util


async def get_network_wireless_ssid_bonjour_forwarding_2(request: web.Request, network_id, number) -> web.Response:
    """List the Bonjour forwarding setting and rules for the SSID

    List the Bonjour forwarding setting and rules for the SSID

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str

    """
    return web.Response(status=200)


async def update_network_wireless_ssid_bonjour_forwarding_2(request: web.Request, network_id, number, body=None) -> web.Response:
    """Update the bonjour forwarding setting and rules for the SSID

    Update the bonjour forwarding setting and rules for the SSID

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkWirelessSsidBonjourForwardingRequest.from_dict(body)
    return web.Response(status=200)

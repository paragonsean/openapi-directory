from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_network_wireless_ssid_hotspot20_request import UpdateNetworkWirelessSsidHotspot20Request
from openapi_server import util


async def get_network_wireless_ssid_hotspot20_2(request: web.Request, network_id, number) -> web.Response:
    """Return the Hotspot 2.0 settings for an SSID

    Return the Hotspot 2.0 settings for an SSID

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str

    """
    return web.Response(status=200)


async def update_network_wireless_ssid_hotspot20_2(request: web.Request, network_id, number, body=None) -> web.Response:
    """Update the Hotspot 2.0 settings of an SSID

    Update the Hotspot 2.0 settings of an SSID

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkWirelessSsidHotspot20Request.from_dict(body)
    return web.Response(status=200)

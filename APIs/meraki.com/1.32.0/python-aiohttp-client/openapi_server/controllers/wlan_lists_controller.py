from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_network_sm_device_wlan_lists200_response_inner import GetNetworkSmDeviceWlanLists200ResponseInner
from openapi_server import util


async def get_network_sm_device_wlan_lists_2(request: web.Request, network_id, device_id) -> web.Response:
    """List the saved SSID names on a device

    List the saved SSID names on a device

    :param network_id: 
    :type network_id: str
    :param device_id: 
    :type device_id: str

    """
    return web.Response(status=200)

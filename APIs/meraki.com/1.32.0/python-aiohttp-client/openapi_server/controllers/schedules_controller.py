from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_network_wireless_ssid_schedules_request import UpdateNetworkWirelessSsidSchedulesRequest
from openapi_server import util


async def get_network_camera_schedules_1(request: web.Request, network_id) -> web.Response:
    """Returns a list of all camera recording schedules.

    Returns a list of all camera recording schedules.

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_wireless_ssid_schedules_2(request: web.Request, network_id, number) -> web.Response:
    """List the outage schedule for the SSID

    List the outage schedule for the SSID

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str

    """
    return web.Response(status=200)


async def update_network_wireless_ssid_schedules_2(request: web.Request, network_id, number, body=None) -> web.Response:
    """Update the outage schedule for the SSID

    Update the outage schedule for the SSID

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkWirelessSsidSchedulesRequest.from_dict(body)
    return web.Response(status=200)

from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_network_ssid_request import UpdateNetworkSsidRequest
from openapi_server import util


async def get_network_device_wireless_status(request: web.Request, network_id, serial) -> web.Response:
    """Return the SSID statuses of an access point

    Return the SSID statuses of an access point

    :param network_id: 
    :type network_id: str
    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_network_ssid(request: web.Request, network_id, number) -> web.Response:
    """Return a single SSID

    Return a single SSID

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str

    """
    return web.Response(status=200)


async def get_network_ssids(request: web.Request, network_id) -> web.Response:
    """List the SSIDs in a network

    List the SSIDs in a network. Supports networks with access points or wireless-enabled security appliances and teleworker gateways.

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def update_network_ssid(request: web.Request, network_id, number, body=None) -> web.Response:
    """Update the attributes of an SSID

    Update the attributes of an SSID

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSsidRequest.from_dict(body)
    return web.Response(status=200)

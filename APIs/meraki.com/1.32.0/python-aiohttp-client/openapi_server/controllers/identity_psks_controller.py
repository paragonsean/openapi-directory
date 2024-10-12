from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_network_wireless_ssid_identity_psk_request import CreateNetworkWirelessSsidIdentityPskRequest
from openapi_server.models.get_network_wireless_ssid_identity_psks200_response_inner import GetNetworkWirelessSsidIdentityPsks200ResponseInner
from openapi_server.models.update_network_wireless_ssid_identity_psk_request import UpdateNetworkWirelessSsidIdentityPskRequest
from openapi_server import util


async def create_network_wireless_ssid_identity_psk_2(request: web.Request, network_id, number, body) -> web.Response:
    """Create an Identity PSK

    Create an Identity PSK

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkWirelessSsidIdentityPskRequest.from_dict(body)
    return web.Response(status=200)


async def delete_network_wireless_ssid_identity_psk_2(request: web.Request, network_id, number, identity_psk_id) -> web.Response:
    """Delete an Identity PSK

    Delete an Identity PSK

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str
    :param identity_psk_id: 
    :type identity_psk_id: str

    """
    return web.Response(status=200)


async def get_network_wireless_ssid_identity_psk_2(request: web.Request, network_id, number, identity_psk_id) -> web.Response:
    """Return an Identity PSK

    Return an Identity PSK

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str
    :param identity_psk_id: 
    :type identity_psk_id: str

    """
    return web.Response(status=200)


async def get_network_wireless_ssid_identity_psks_2(request: web.Request, network_id, number) -> web.Response:
    """List all Identity PSKs in a wireless network

    List all Identity PSKs in a wireless network

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str

    """
    return web.Response(status=200)


async def update_network_wireless_ssid_identity_psk_2(request: web.Request, network_id, number, identity_psk_id, body=None) -> web.Response:
    """Update an Identity PSK

    Update an Identity PSK

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str
    :param identity_psk_id: 
    :type identity_psk_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkWirelessSsidIdentityPskRequest.from_dict(body)
    return web.Response(status=200)

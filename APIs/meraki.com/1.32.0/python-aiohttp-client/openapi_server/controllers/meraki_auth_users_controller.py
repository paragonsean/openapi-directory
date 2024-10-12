from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_network_meraki_auth_user_request import CreateNetworkMerakiAuthUserRequest
from openapi_server.models.get_network_meraki_auth_users200_response_inner import GetNetworkMerakiAuthUsers200ResponseInner
from openapi_server.models.update_network_meraki_auth_user_request import UpdateNetworkMerakiAuthUserRequest
from openapi_server import util


async def create_network_meraki_auth_user_1(request: web.Request, network_id, body) -> web.Response:
    """Authorize a user configured with Meraki Authentication for a network (currently supports 802.1X, splash guest, and client VPN users, and currently, organizations have a 50,000 user cap)

    Authorize a user configured with Meraki Authentication for a network (currently supports 802.1X, splash guest, and client VPN users, and currently, organizations have a 50,000 user cap)

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkMerakiAuthUserRequest.from_dict(body)
    return web.Response(status=200)


async def delete_network_meraki_auth_user_1(request: web.Request, network_id, meraki_auth_user_id) -> web.Response:
    """Deauthorize a user

    Deauthorize a user. To reauthorize a user after deauthorizing them, POST to this endpoint. (Currently, 802.1X RADIUS, splash guest, and client VPN users can be deauthorized.)

    :param network_id: 
    :type network_id: str
    :param meraki_auth_user_id: 
    :type meraki_auth_user_id: str

    """
    return web.Response(status=200)


async def get_network_meraki_auth_user_1(request: web.Request, network_id, meraki_auth_user_id) -> web.Response:
    """Return the Meraki Auth splash guest, RADIUS, or client VPN user

    Return the Meraki Auth splash guest, RADIUS, or client VPN user

    :param network_id: 
    :type network_id: str
    :param meraki_auth_user_id: 
    :type meraki_auth_user_id: str

    """
    return web.Response(status=200)


async def get_network_meraki_auth_users_1(request: web.Request, network_id) -> web.Response:
    """List the users configured under Meraki Authentication for a network (splash guest or RADIUS users for a wireless network, or client VPN users for a wired network)

    List the users configured under Meraki Authentication for a network (splash guest or RADIUS users for a wireless network, or client VPN users for a wired network)

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def update_network_meraki_auth_user_1(request: web.Request, network_id, meraki_auth_user_id, body=None) -> web.Response:
    """Update a user configured with Meraki Authentication (currently, 802.1X RADIUS, splash guest, and client VPN users can be updated)

    Update a user configured with Meraki Authentication (currently, 802.1X RADIUS, splash guest, and client VPN users can be updated)

    :param network_id: 
    :type network_id: str
    :param meraki_auth_user_id: 
    :type meraki_auth_user_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkMerakiAuthUserRequest.from_dict(body)
    return web.Response(status=200)

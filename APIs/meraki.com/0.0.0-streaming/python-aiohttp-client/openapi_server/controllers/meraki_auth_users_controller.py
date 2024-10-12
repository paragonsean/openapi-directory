from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_network_meraki_auth_user(request: web.Request, network_id, meraki_auth_user_id) -> web.Response:
    """Return the Meraki Auth splash or RADIUS user

    Return the Meraki Auth splash or RADIUS user

    :param network_id: 
    :type network_id: str
    :param meraki_auth_user_id: 
    :type meraki_auth_user_id: str

    """
    return web.Response(status=200)


async def get_network_meraki_auth_users(request: web.Request, network_id) -> web.Response:
    """List the splash or RADIUS users configured under Meraki Authentication for a network

    List the splash or RADIUS users configured under Meraki Authentication for a network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)

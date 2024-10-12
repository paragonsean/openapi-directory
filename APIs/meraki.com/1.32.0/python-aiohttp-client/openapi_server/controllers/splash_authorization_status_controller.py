from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_network_client_splash_authorization_status_request import UpdateNetworkClientSplashAuthorizationStatusRequest
from openapi_server import util


async def get_network_client_splash_authorization_status_2(request: web.Request, network_id, client_id) -> web.Response:
    """Return the splash authorization for a client, for each SSID they&#39;ve associated with through splash

    Return the splash authorization for a client, for each SSID they&#39;ve associated with through splash. Only enabled SSIDs with Click-through splash enabled will be included. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.

    :param network_id: 
    :type network_id: str
    :param client_id: 
    :type client_id: str

    """
    return web.Response(status=200)


async def update_network_client_splash_authorization_status_2(request: web.Request, network_id, client_id, body) -> web.Response:
    """Update a client&#39;s splash authorization

    Update a client&#39;s splash authorization. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.

    :param network_id: 
    :type network_id: str
    :param client_id: 
    :type client_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkClientSplashAuthorizationStatusRequest.from_dict(body)
    return web.Response(status=200)

from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_network_client_policy_request import UpdateNetworkClientPolicyRequest
from openapi_server import util


async def get_network_client_policy_2(request: web.Request, network_id, client_id) -> web.Response:
    """Return the policy assigned to a client on the network

    Return the policy assigned to a client on the network. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.

    :param network_id: 
    :type network_id: str
    :param client_id: 
    :type client_id: str

    """
    return web.Response(status=200)


async def update_network_client_policy_2(request: web.Request, network_id, client_id, body) -> web.Response:
    """Update the policy assigned to a client on the network

    Update the policy assigned to a client on the network. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.

    :param network_id: 
    :type network_id: str
    :param client_id: 
    :type client_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkClientPolicyRequest.from_dict(body)
    return web.Response(status=200)

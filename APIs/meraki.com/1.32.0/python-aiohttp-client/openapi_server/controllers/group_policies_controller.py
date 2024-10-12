from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_network_group_policy_request import CreateNetworkGroupPolicyRequest
from openapi_server.models.update_network_group_policy_request import UpdateNetworkGroupPolicyRequest
from openapi_server import util


async def create_network_group_policy_1(request: web.Request, network_id, body) -> web.Response:
    """Create a group policy

    Create a group policy

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkGroupPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def delete_network_group_policy_1(request: web.Request, network_id, group_policy_id) -> web.Response:
    """Delete a group policy

    Delete a group policy

    :param network_id: 
    :type network_id: str
    :param group_policy_id: 
    :type group_policy_id: str

    """
    return web.Response(status=200)


async def get_network_group_policies_1(request: web.Request, network_id) -> web.Response:
    """List the group policies in a network

    List the group policies in a network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_group_policy_1(request: web.Request, network_id, group_policy_id) -> web.Response:
    """Display a group policy

    Display a group policy

    :param network_id: 
    :type network_id: str
    :param group_policy_id: 
    :type group_policy_id: str

    """
    return web.Response(status=200)


async def update_network_group_policy_1(request: web.Request, network_id, group_policy_id, body=None) -> web.Response:
    """Update a group policy

    Update a group policy

    :param network_id: 
    :type network_id: str
    :param group_policy_id: 
    :type group_policy_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkGroupPolicyRequest.from_dict(body)
    return web.Response(status=200)

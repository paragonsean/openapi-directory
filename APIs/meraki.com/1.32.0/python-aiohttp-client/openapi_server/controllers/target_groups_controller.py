from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_network_sm_target_group_request import CreateNetworkSmTargetGroupRequest
from openapi_server import util


async def create_network_sm_target_group_1(request: web.Request, network_id, body=None) -> web.Response:
    """Add a target group

    Add a target group

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkSmTargetGroupRequest.from_dict(body)
    return web.Response(status=200)


async def delete_network_sm_target_group_1(request: web.Request, network_id, target_group_id) -> web.Response:
    """Delete a target group from a network

    Delete a target group from a network

    :param network_id: 
    :type network_id: str
    :param target_group_id: 
    :type target_group_id: str

    """
    return web.Response(status=200)


async def get_network_sm_target_group_1(request: web.Request, network_id, target_group_id, with_details=None) -> web.Response:
    """Return a target group

    Return a target group

    :param network_id: 
    :type network_id: str
    :param target_group_id: 
    :type target_group_id: str
    :param with_details: Boolean indicating if the the ids of the devices or users scoped by the target group should be included in the response
    :type with_details: bool

    """
    return web.Response(status=200)


async def get_network_sm_target_groups_1(request: web.Request, network_id, with_details=None) -> web.Response:
    """List the target groups in this network

    List the target groups in this network

    :param network_id: 
    :type network_id: str
    :param with_details: Boolean indicating if the the ids of the devices or users scoped by the target group should be included in the response
    :type with_details: bool

    """
    return web.Response(status=200)


async def update_network_sm_target_group_1(request: web.Request, network_id, target_group_id, body=None) -> web.Response:
    """Update a target group

    Update a target group

    :param network_id: 
    :type network_id: str
    :param target_group_id: 
    :type target_group_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkSmTargetGroupRequest.from_dict(body)
    return web.Response(status=200)

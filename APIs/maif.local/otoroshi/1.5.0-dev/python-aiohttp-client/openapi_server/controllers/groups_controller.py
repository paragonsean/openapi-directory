from typing import List, Dict
from aiohttp import web

from openapi_server.models.deleted import Deleted
from openapi_server.models.group import Group
from openapi_server.models.patch_inner import PatchInner
from openapi_server import util


async def all_service_groups(request: web.Request, ) -> web.Response:
    """Get all service groups

    Get all service groups


    """
    return web.Response(status=200)


async def create_group(request: web.Request, body=None) -> web.Response:
    """Create a new service group

    Create a new service group

    :param body: 
    :type body: dict | bytes

    """
    body = Group.from_dict(body)
    return web.Response(status=200)


async def delete_group(request: web.Request, service_group_id) -> web.Response:
    """Delete a service group

    Delete a service group

    :param service_group_id: The service group id
    :type service_group_id: str

    """
    return web.Response(status=200)


async def patch_group(request: web.Request, service_group_id, body=None) -> web.Response:
    """Update a service group with a diff

    Update a service group with a diff

    :param service_group_id: The service group id
    :type service_group_id: str
    :param body: 
    :type body: list | bytes

    """
    body = [PatchInner.from_dict(d) for d in body]
    return web.Response(status=200)


async def service_group(request: web.Request, service_group_id) -> web.Response:
    """Get a service group

    Get a service group

    :param service_group_id: The service group id
    :type service_group_id: str

    """
    return web.Response(status=200)


async def update_group(request: web.Request, service_group_id, body=None) -> web.Response:
    """Update a service group

    Update a service group

    :param service_group_id: The service group id
    :type service_group_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Group.from_dict(body)
    return web.Response(status=200)

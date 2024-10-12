from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.role import Role
from openapi_server.models.role_addition import RoleAddition
from openapi_server.models.role_with_groups import RoleWithGroups
from openapi_server import util


async def add_role(request: web.Request, body) -> web.Response:
    """Add role

    

    :param body: 
    :type body: dict | bytes

    """
    body = RoleAddition.from_dict(body)
    return web.Response(status=200)


async def delete_role(request: web.Request, role_id) -> web.Response:
    """Delete role

    

    :param role_id: Role ID
    :type role_id: int

    """
    return web.Response(status=200)


async def get_role(request: web.Request, role_id) -> web.Response:
    """Get role

    

    :param role_id: Role ID
    :type role_id: int

    """
    return web.Response(status=200)


async def get_roles(request: web.Request, ) -> web.Response:
    """Get roles

    


    """
    return web.Response(status=200)


async def update_role(request: web.Request, body) -> web.Response:
    """Update role

    

    :param body: 
    :type body: dict | bytes

    """
    body = RoleWithGroups.from_dict(body)
    return web.Response(status=200)

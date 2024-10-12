from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.role import Role
from openapi_server.models.role_collection import RoleCollection
from openapi_server import util


async def delete_role(request: web.Request, role_name) -> web.Response:
    """Delete a role

    Delete a role.  *New in version 2.1.0* 

    :param role_name: The role name
    :type role_name: str

    """
    return web.Response(status=200)


async def get_role(request: web.Request, role_name) -> web.Response:
    """Get a role

    Get a role.  *New in version 2.1.0* 

    :param role_name: The role name
    :type role_name: str

    """
    return web.Response(status=200)


async def get_roles(request: web.Request, limit=None, offset=None, order_by=None) -> web.Response:
    """List roles

    Get a list of roles.  *New in version 2.1.0* 

    :param limit: The numbers of items to return.
    :type limit: int
    :param offset: The number of items to skip before starting to collect the result set.
    :type offset: int
    :param order_by: The name of the field to order the results by. Prefix a field name with &#x60;-&#x60; to reverse the sort order.  *New in version 2.1.0* 
    :type order_by: str

    """
    return web.Response(status=200)


async def patch_role(request: web.Request, role_name, body, update_mask=None) -> web.Response:
    """Update a role

    Update a role.  *New in version 2.1.0* 

    :param role_name: The role name
    :type role_name: str
    :param body: 
    :type body: dict | bytes
    :param update_mask: The fields to update on the resource. If absent or empty, all modifiable fields are updated. A comma-separated list of fully qualified names of fields. 
    :type update_mask: List[str]

    """
    body = Role.from_dict(body)
    return web.Response(status=200)


async def post_role(request: web.Request, body) -> web.Response:
    """Create a role

    Create a new role.  *New in version 2.1.0* 

    :param body: 
    :type body: dict | bytes

    """
    body = Role.from_dict(body)
    return web.Response(status=200)

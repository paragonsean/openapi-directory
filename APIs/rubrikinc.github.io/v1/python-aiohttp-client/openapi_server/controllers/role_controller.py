from typing import List, Dict
from aiohttp import web

from openapi_server.models.role_info import RoleInfo
from openapi_server.models.role_info_create import RoleInfoCreate
from openapi_server.models.role_info_list_response import RoleInfoListResponse
from openapi_server.models.role_info_update import RoleInfoUpdate
from openapi_server import util


async def create_role(request: web.Request, body) -> web.Response:
    """Create a new role

    Create a new role in the current organization.

    :param body: Information about the role.
    :type body: dict | bytes

    """
    body = RoleInfoCreate.from_dict(body)
    return web.Response(status=200)


async def delete_role(request: web.Request, id) -> web.Response:
    """Delete a role

    Delete the role with the specified ID.

    :param id: ID of the role.
    :type id: str

    """
    return web.Response(status=200)


async def get_role(request: web.Request, id) -> web.Response:
    """Get role information for the specified role

    Get role information for the role with the specified ID.

    :param id: ID of the role.
    :type id: str

    """
    return web.Response(status=200)


async def get_roles(request: web.Request, limit=None, offset=None, sort_by=None, sort_order=None, organization_id=None, name=None, role_template=None) -> web.Response:
    """Get all roles in an organization

    Get a list of role information for all roles in the specified organization. 

    :param limit: Maximum number of results to return.
    :type limit: int
    :param offset: Starting offset of the results to return.
    :type offset: int
    :param sort_by: Attribute used to sort the role list.
    :type sort_by: str
    :param sort_order: Sort order used, ascending or descending.
    :type sort_order: str
    :param organization_id: The ID of the organization the roles are a part of. When empty, the Rubrik cluster infers the organization from the session. 
    :type organization_id: str
    :param name: The name of the role.
    :type name: str
    :param role_template: List of comma-separated role templates by which to filter the roles. 
    :type role_template: List[str]

    """
    return web.Response(status=200)


async def update_role(request: web.Request, id, body) -> web.Response:
    """Update role information

    Update the role information for the specified role.

    :param id: ID of the role.
    :type id: str
    :param body: Information about the role.
    :type body: dict | bytes

    """
    body = RoleInfoUpdate.from_dict(body)
    return web.Response(status=200)

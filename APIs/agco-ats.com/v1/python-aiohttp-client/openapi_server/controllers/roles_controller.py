from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_models_role import APIModelsRole
from openapi_server.models.api_models_role_permission_change import APIModelsRolePermissionChange
from openapi_server.models.api_paged_response_api_models_permission import APIPagedResponseAPIModelsPermission
from openapi_server.models.api_paged_response_api_models_role import APIPagedResponseAPIModelsRole
from openapi_server import util


async def roles_delete_role(request: web.Request, id) -> web.Response:
    """Deletes a User Role

    No Documentation Found.

    :param id: The role&#39;s id
    :type id: int

    """
    return web.Response(status=200)


async def roles_get_role(request: web.Request, id) -> web.Response:
    """Gets a User Role

    No Documentation Found.

    :param id: The role&#39;s id
    :type id: int

    """
    return web.Response(status=200)


async def roles_get_role_permissions(request: web.Request, id, name=None, limit=None, offset=None) -> web.Response:
    """Get the Permissions for a Role

    No Documentation Found.

    :param id: The id of the Role
    :type id: int
    :param name: Filter by permission name. Optional.
    :type name: str
    :param limit: Optional. The page limit. The default page limit is 10.
    :type limit: int
    :param offset: Optional. The page offset. The default page offset is 0.
    :type offset: int

    """
    return web.Response(status=200)


async def roles_get_roles(request: web.Request, limit=None, offset=None, name=None, permission_id=None, permission_name=None) -> web.Response:
    """List Roles

    No Documentation Found.

    :param limit: Optional. The page limit. The default page limit is 10.
    :type limit: int
    :param offset: Optional. The page offset. The default page offset is 0.
    :type offset: int
    :param name: Optional. Finds a role with the given name.
    :type name: str
    :param permission_id: 
    :type permission_id: int
    :param permission_name: Optional. Filters roles by whether they contain the provided permission.
    :type permission_name: str

    """
    return web.Response(status=200)


async def roles_post_role(request: web.Request, body) -> web.Response:
    """Adds a User Role

    No Documentation Found.

    :param body: Role to add
    :type body: dict | bytes

    """
    body = APIModelsRole.from_dict(body)
    return web.Response(status=200)


async def roles_put_role(request: web.Request, id, body) -> web.Response:
    """Updates a User Role

    No Documentation Found.

    :param id: The role&#39;s id
    :type id: int
    :param body: The Updated Role
    :type body: dict | bytes

    """
    body = APIModelsRole.from_dict(body)
    return web.Response(status=200)


async def roles_put_role_permissions(request: web.Request, id, body) -> web.Response:
    """Manage the Permissions for a Role

    No Documentation Found.

    :param id: The id of the Role
    :type id: int
    :param body: Permissions Changes for the Role
    :type body: list | bytes

    """
    body = [APIModelsRolePermissionChange.from_dict(d) for d in body]
    return web.Response(status=200)

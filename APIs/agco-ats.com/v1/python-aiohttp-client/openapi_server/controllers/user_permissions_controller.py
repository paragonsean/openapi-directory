from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.api_models_role_user_change import APIModelsRoleUserChange
from openapi_server.models.api_models_user_role_change import APIModelsUserRoleChange
from openapi_server.models.api_paged_response_api_models_role import APIPagedResponseAPIModelsRole
from openapi_server.models.api_paged_response_api_models_user import APIPagedResponseAPIModelsUser
from openapi_server.models.api_paged_response_api_models_user_effective_permission import APIPagedResponseAPIModelsUserEffectivePermission
from openapi_server import util


async def api_v2_roles_id_users_put(request: web.Request, id, body) -> web.Response:
    """Update a Role&#39;s users

    No Documentation Found.

    :param id: The Role&#39;s ID
    :type id: int
    :param body: A list of changes to the Role&#39;s Users
    :type body: list | bytes

    """
    body = [APIModelsRoleUserChange.from_dict(d) for d in body]
    return web.Response(status=200)


async def api_v2_users_current_permissions_get(request: web.Request, permission=None, limit=None, offset=None) -> web.Response:
    """Get a user&#39;s permissions

    No Documentation Found.

    :param permission: Filter by permission name. Supports ending wildcard (*). Optional.
    :type permission: str
    :param limit: The page limit. The default page limit is 10.
    :type limit: int
    :param offset: The page offset. The default page offset is 0.
    :type offset: int

    """
    return web.Response(status=200)


async def user_permissions_get_current_user_roles(request: web.Request, role=None, limit=None, offset=None) -> web.Response:
    """Gets the current user&#39;s roles

    No Documentation Found.

    :param role: Filter by role name. Supports ending wildcard (*). Optional.
    :type role: str
    :param limit: The page limit. The default page limit is 10.
    :type limit: int
    :param offset: The page offset. The default page offset is 0.
    :type offset: int

    """
    return web.Response(status=200)


async def user_permissions_get_permissions(request: web.Request, id, permission=None, limit=None, offset=None) -> web.Response:
    """Get a user&#39;s permissions

    No Documentation Found.

    :param id: The User&#39;s ID
    :type id: int
    :param permission: Filter by permission name. Supports ending wildcard (*). Optional.
    :type permission: str
    :param limit: The page limit. The default page limit is 10.
    :type limit: int
    :param offset: The page offset. The default page offset is 0.
    :type offset: int

    """
    return web.Response(status=200)


async def user_permissions_get_roles(request: web.Request, id, role=None, limit=None, offset=None) -> web.Response:
    """Get a user&#39;s roles

    No Documentation Found.

    :param id: The User&#39;s ID
    :type id: int
    :param role: Filter by role name. Supports ending wildcard (*). Optional.
    :type role: str
    :param limit: The page limit. The default page limit is 10.
    :type limit: int
    :param offset: The page offset. The default page offset is 0.
    :type offset: int

    """
    return web.Response(status=200)


async def user_permissions_get_users(request: web.Request, id, limit=None, offset=None) -> web.Response:
    """Get all user&#39;s in a role

    No Documentation Found.

    :param id: The Role&#39;s ID
    :type id: int
    :param limit: The page limit. The default page limit is 10.
    :type limit: int
    :param offset: The page offset. The default page offset is 0.
    :type offset: int

    """
    return web.Response(status=200)


async def user_permissions_put(request: web.Request, id, body) -> web.Response:
    """Update a user&#39;s roles

    No Documentation Found.

    :param id: The User&#39;s ID
    :type id: int
    :param body: A list of changes to the User&#39;s Roles
    :type body: list | bytes

    """
    body = [APIModelsUserRoleChange.from_dict(d) for d in body]
    return web.Response(status=200)

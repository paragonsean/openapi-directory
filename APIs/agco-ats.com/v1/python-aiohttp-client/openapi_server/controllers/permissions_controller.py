from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_models_permission import APIModelsPermission
from openapi_server.models.api_paged_response_api_models_permission import APIPagedResponseAPIModelsPermission
from openapi_server import util


async def permissions_delete_permission(request: web.Request, id) -> web.Response:
    """Deletes a Permission

    No Documentation Found.

    :param id: Id of Permission
    :type id: int

    """
    return web.Response(status=200)


async def permissions_get_permission(request: web.Request, id) -> web.Response:
    """Gets a Permission

    No Documentation Found.

    :param id: Id of Permission
    :type id: int

    """
    return web.Response(status=200)


async def permissions_get_permissions(request: web.Request, limit=None, offset=None, name=None) -> web.Response:
    """List Permissions

    No Documentation Found.

    :param limit: Optional. The page limit. The default page limit is 10.
    :type limit: int
    :param offset: Optional. The page offset. The default page offset is 0.
    :type offset: int
    :param name: Filter by permission name. Supports ending wildcard (*). Optional.
    :type name: str

    """
    return web.Response(status=200)


async def permissions_post_permission(request: web.Request, body) -> web.Response:
    """Adds a Permission

    No Documentation Found.

    :param body: Permission to add
    :type body: dict | bytes

    """
    body = APIModelsPermission.from_dict(body)
    return web.Response(status=200)


async def permissions_put_permission(request: web.Request, id, body) -> web.Response:
    """Updates a Permission

    No Documentation Found.

    :param id: Id of Permission
    :type id: int
    :param body: The Updated Permission
    :type body: dict | bytes

    """
    body = APIModelsPermission.from_dict(body)
    return web.Response(status=200)

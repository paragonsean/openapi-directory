from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_models_user import APIModelsUser
from openapi_server.models.api_paged_response_api_models_user import APIPagedResponseAPIModelsUser
from openapi_server import util


async def api_v2_users_id_get(request: web.Request, id) -> web.Response:
    """Get a specific user

    No Documentation Found.

    :param id: The user ID
    :type id: int

    """
    return web.Response(status=200)


async def users_delete(request: web.Request, id) -> web.Response:
    """Delete a user

    No Documentation Found.

    :param id: The user id
    :type id: int

    """
    return web.Response(status=200)


async def users_get(request: web.Request, username=None, email=None, name=None, has_role=None, limit=None, offset=None) -> web.Response:
    """Get users

    No Documentation Found.

    :param username: Optional. Search by username. Supports beginning and ending wildcards (*).
    :type username: str
    :param email: Optional. Search by email. Supports beginning and ending wildcards (*).
    :type email: str
    :param name: Optional. Search by name. Supports beginning and ending wildcards (*).
    :type name: str
    :param has_role: Optional. Return only users having the provided role name.
    :type has_role: str
    :param limit: Optional. The page limit. The default page limit is 10.
    :type limit: int
    :param offset: Optional. The page offset. The default page offset is 0.
    :type offset: int

    """
    return web.Response(status=200)


async def users_get_current_user(request: web.Request, ) -> web.Response:
    """Gets the current user

    No Documentation Found.


    """
    return web.Response(status=200)


async def users_post(request: web.Request, body) -> web.Response:
    """Create a user

    No Documentation Found.

    :param body: The user to create.
    :type body: dict | bytes

    """
    body = APIModelsUser.from_dict(body)
    return web.Response(status=200)


async def users_put(request: web.Request, id, body) -> web.Response:
    """Update a user

    No Documentation Found.

    :param id: The user id
    :type id: int
    :param body: The user
    :type body: dict | bytes

    """
    body = APIModelsUser.from_dict(body)
    return web.Response(status=200)


async def users_put_current_user(request: web.Request, body) -> web.Response:
    """Update a user

    No Documentation Found.

    :param body: The user
    :type body: dict | bytes

    """
    body = APIModelsUser.from_dict(body)
    return web.Response(status=200)

from typing import List, Dict
from aiohttp import web

from openapi_server.models.json_user import JsonUser
from openapi_server import util


async def resource10_user_user_id_get_user_get(request: web.Request, user_id) -> web.Response:
    """Get a user by userId.

    Get a user by userId. (deprecated)  Note: This endpoint always returns a result, even if the user doesn&#39;t exist

    :param user_id: the user&#39;s userId
    :type user_id: str

    """
    return web.Response(status=200)

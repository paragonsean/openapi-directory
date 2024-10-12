from typing import List, Dict
from aiohttp import web

from openapi_server.models.user import User
from openapi_server import util


async def users_id_get(request: web.Request, id) -> web.Response:
    """Get user profile

    Get profile a user

    :param id: Id of user
    :type id: int

    """
    return web.Response(status=200)

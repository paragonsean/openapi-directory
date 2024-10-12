from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.user_info import UserInfo
from openapi_server import util


async def get_current_user_info(request: web.Request, ) -> web.Response:
    """Get current user

    Returns information about the currently authenticated user.


    """
    return web.Response(status=200)

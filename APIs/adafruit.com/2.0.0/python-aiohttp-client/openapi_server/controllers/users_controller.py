from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_current_user_throttle200_response import GetCurrentUserThrottle200Response
from openapi_server.models.user import User
from openapi_server import util


async def current_user(request: web.Request, ) -> web.Response:
    """Get information about the current user

    


    """
    return web.Response(status=200)


async def get_current_user_throttle(request: web.Request, username) -> web.Response:
    """Get the user&#39;s data rate limit and current activity level.

    

    :param username: a valid username string
    :type username: str

    """
    return web.Response(status=200)

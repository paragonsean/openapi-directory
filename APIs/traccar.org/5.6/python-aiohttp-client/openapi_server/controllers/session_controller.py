from typing import List, Dict
from aiohttp import web

from openapi_server.models.user import User
from openapi_server import util


async def session_delete(request: web.Request, ) -> web.Response:
    """Close the Session

    


    """
    return web.Response(status=200)


async def session_get(request: web.Request, token=None) -> web.Response:
    """Fetch Session information

    

    :param token: 
    :type token: str

    """
    return web.Response(status=200)


async def session_post(request: web.Request, email, password) -> web.Response:
    """Create a new Session

    

    :param email: 
    :type email: str
    :param password: 
    :type password: str

    """
    return web.Response(status=200)

from typing import List, Dict
from aiohttp import web

from openapi_server.models.check_get_default_response import CheckGetDefaultResponse
from openapi_server import util


async def pve_info_get(request: web.Request, ) -> web.Response:
    """Get Fortnite PVE Info (storm, etc)

    


    """
    return web.Response(status=200)


async def pve_user_username_get(request: web.Request, username) -> web.Response:
    """Get PVE Stat by given username

    

    :param username: Fortnite username
    :type username: str

    """
    return web.Response(status=200)

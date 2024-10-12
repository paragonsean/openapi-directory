from typing import List, Dict
from aiohttp import web

from openapi_server.models.user import User
from openapi_server import util


async def who_am_i(request: web.Request, ) -> web.Response:
    """who_am_i

    Get information about the user you are authenticated as. Authorized for admins, editors, operators, and kiosk.


    """
    return web.Response(status=200)

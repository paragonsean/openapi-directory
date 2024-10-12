from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def contacts_get(request: web.Request, ) -> web.Response:
    """View all contacts under your account

    Shows all contacts under the client account.


    """
    return web.Response(status=200)

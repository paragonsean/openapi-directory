from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def do_log_out(request: web.Request, ) -> web.Response:
    """do_log_out

    Logout from the bank


    """
    return web.Response(status=200)

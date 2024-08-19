from typing import List, Dict
from aiohttp import web

from openapi_server.models.account import Account
from openapi_server.models.error import Error
from openapi_server import util


async def account(request: web.Request, ) -> web.Response:
    """Information about your account calls quota

    Always returns JSON


    """
    return web.Response(status=200)

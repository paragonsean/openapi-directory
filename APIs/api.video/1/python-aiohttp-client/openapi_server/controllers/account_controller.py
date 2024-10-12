from typing import List, Dict
from aiohttp import web

from openapi_server.models.account import Account
from openapi_server.models.not_found import NotFound
from openapi_server import util


async def g_et_account(request: web.Request, ) -> web.Response:
    """Show account

    Deprecated. Authenticate and get a token, then you can use the bearer token here to retrieve details about your account.


    """
    return web.Response(status=200)

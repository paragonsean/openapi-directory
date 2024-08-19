from typing import List, Dict
from aiohttp import web

from openapi_server.models.account import Account
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def get_account(request: web.Request, ) -> web.Response:
    """Account info

    


    """
    return web.Response(status=200)

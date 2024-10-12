from typing import List, Dict
from aiohttp import web

from openapi_server.models.account_details import AccountDetails
from openapi_server import util


async def account_get(request: web.Request, ) -> web.Response:
    """Account Details

    


    """
    return web.Response(status=200)

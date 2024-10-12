from typing import List, Dict
from aiohttp import web

from openapi_server.models.account_type import AccountType
from openapi_server.models.error import Error
from openapi_server import util


async def list_account_types_for_user(request: web.Request, ) -> web.Response:
    """list_account_types_for_user

    


    """
    return web.Response(status=200)

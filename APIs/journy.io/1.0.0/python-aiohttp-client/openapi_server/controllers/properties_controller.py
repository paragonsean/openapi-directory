from typing import List, Dict
from aiohttp import web

from openapi_server.models.delete_account202_response import DeleteAccount202Response
from openapi_server.models.delete_account400_response import DeleteAccount400Response
from openapi_server.models.get_account_properties200_response import GetAccountProperties200Response
from openapi_server import util


async def get_account_properties(request: web.Request, ) -> web.Response:
    """Get account properties

    Endpoint to list account properties.


    """
    return web.Response(status=200)


async def get_user_properties(request: web.Request, ) -> web.Response:
    """Get user properties

    Endpoint to list user properties.


    """
    return web.Response(status=200)

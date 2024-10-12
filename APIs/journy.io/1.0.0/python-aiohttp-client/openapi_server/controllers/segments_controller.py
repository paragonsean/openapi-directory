from typing import List, Dict
from aiohttp import web

from openapi_server.models.delete_account202_response import DeleteAccount202Response
from openapi_server.models.delete_account400_response import DeleteAccount400Response
from openapi_server.models.get_account_segments200_response import GetAccountSegments200Response
from openapi_server import util


async def get_account_segments(request: web.Request, ) -> web.Response:
    """Get account segments

    Endpoint to list account segments.


    """
    return web.Response(status=200)


async def get_user_segments(request: web.Request, ) -> web.Response:
    """Get user segments

    Endpoint to list user segments.


    """
    return web.Response(status=200)

from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.user import User
from openapi_server import util


async def get_user(request: web.Request, ) -> web.Response:
    """User info

    


    """
    return web.Response(status=200)

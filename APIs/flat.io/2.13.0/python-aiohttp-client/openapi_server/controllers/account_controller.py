from typing import List, Dict
from aiohttp import web

from openapi_server.models.flat_error_response import FlatErrorResponse
from openapi_server.models.user_details import UserDetails
from openapi_server import util


async def get_authenticated_user(request: web.Request, only_id=None) -> web.Response:
    """Get current user profile

    Get details about the current authenticated User. 

    :param only_id: Only return the user id
    :type only_id: bool

    """
    return web.Response(status=200)

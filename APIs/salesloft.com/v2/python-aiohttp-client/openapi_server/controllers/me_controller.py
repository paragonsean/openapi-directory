from typing import List, Dict
from aiohttp import web

from openapi_server.models.user import User
from openapi_server import util


async def v2_me_json_get(request: web.Request, ) -> web.Response:
    """Fetch current user

    Authenticated user information. This endpoint does not accept any parameters as it is represents your authenticated user. The \&quot;Users\&quot; resource provides user information for other users on the team. 


    """
    return web.Response(status=200)

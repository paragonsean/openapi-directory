from typing import List, Dict
from aiohttp import web

from openapi_server.models.label import Label
from openapi_server import util


async def get_active_sessions(request: web.Request, ) -> web.Response:
    """Gets a list of active sessions

    Gets a list of active RTCsessions OauthScopes: CALLS


    """
    return web.Response(status=200)

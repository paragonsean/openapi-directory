from typing import List, Dict
from aiohttp import web

from openapi_server.models.team import Team
from openapi_server import util


async def v2_team_json_get(request: web.Request, ) -> web.Response:
    """Fetch current team

    Fetches the team of the authenticated user. 


    """
    return web.Response(status=200)

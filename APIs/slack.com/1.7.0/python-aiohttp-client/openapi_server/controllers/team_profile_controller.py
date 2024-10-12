from typing import List, Dict
from aiohttp import web

from openapi_server.models.team_profile_get_error_schema import TeamProfileGetErrorSchema
from openapi_server.models.team_profile_get_success_schema import TeamProfileGetSuccessSchema
from openapi_server import util


async def team_profile_get(request: web.Request, token, visibility=None) -> web.Response:
    """team_profile_get

    Retrieve a team&#39;s profile.

    :param token: Authentication token. Requires scope: &#x60;users.profile:read&#x60;
    :type token: str
    :param visibility: Filter by visibility.
    :type visibility: str

    """
    return web.Response(status=200)

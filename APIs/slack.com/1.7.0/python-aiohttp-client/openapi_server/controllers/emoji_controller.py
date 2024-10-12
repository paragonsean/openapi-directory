from typing import List, Dict
from aiohttp import web

from openapi_server.models.default_error_template import DefaultErrorTemplate
from openapi_server.models.default_success_template import DefaultSuccessTemplate
from openapi_server import util


async def emoji_list(request: web.Request, token) -> web.Response:
    """emoji_list

    Lists custom emoji for a team.

    :param token: Authentication token. Requires scope: &#x60;emoji:read&#x60;
    :type token: str

    """
    return web.Response(status=200)

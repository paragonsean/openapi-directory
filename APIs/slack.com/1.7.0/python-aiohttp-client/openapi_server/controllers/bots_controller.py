from typing import List, Dict
from aiohttp import web

from openapi_server.models.bots_info_error_schema import BotsInfoErrorSchema
from openapi_server.models.bots_info_schema import BotsInfoSchema
from openapi_server import util


async def bots_info(request: web.Request, token, bot=None) -> web.Response:
    """bots_info

    Gets information about a bot user.

    :param token: Authentication token. Requires scope: &#x60;users:read&#x60;
    :type token: str
    :param bot: Bot user to get info on
    :type bot: str

    """
    return web.Response(status=200)

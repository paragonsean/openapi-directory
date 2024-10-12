from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def api_v20_login_get(request: web.Request, password=None, username=None) -> web.Response:
    """api_v20_login_get

    Login endpoint, refresh your API token

    :param password: EnteroBase Password
    :type password: str
    :param username: EnteroBase username
    :type username: str

    """
    return web.Response(status=200)

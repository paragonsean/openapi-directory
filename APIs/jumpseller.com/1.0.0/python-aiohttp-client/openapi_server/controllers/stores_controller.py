from typing import List, Dict
from aiohttp import web

from openapi_server.models.language import Language
from openapi_server.models.store import Store
from openapi_server import util


async def store_info_json_get(request: web.Request, login, authtoken) -> web.Response:
    """Retrieve Store Information.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str

    """
    return web.Response(status=200)


async def store_languages_json_get(request: web.Request, login, authtoken) -> web.Response:
    """Retrieve Store Languages.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str

    """
    return web.Response(status=200)

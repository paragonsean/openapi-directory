from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_languages(request: web.Request, type, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get languages

    Get a list of all langauges, including names and codes.

    :param type: 
    :type type: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)

from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_genres(request: web.Request, type, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get genres

    Get a list of all genres, including names and slugs.

    :param type: 
    :type type: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)

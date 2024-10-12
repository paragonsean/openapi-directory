from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_networks(request: web.Request, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get networks

    Get a list of all TV networks, including the name.

    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)

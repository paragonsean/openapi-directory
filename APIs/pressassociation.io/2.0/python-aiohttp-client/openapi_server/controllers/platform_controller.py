from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_platform(request: web.Request, platform_id) -> web.Response:
    """Platform Detail

    Return the content of the selected platform.

    :param platform_id: The identifier for the selected platform.
    :type platform_id: str

    """
    return web.Response(status=200)


async def list_platform_regions(request: web.Request, platform_id, aliases=None) -> web.Response:
    """Platform Region Collection

    Return a list of regions for a platform.

    :param platform_id: The identifier for the selected platform.
    :type platform_id: str
    :param aliases: Flag to display Legacy and Provider Ids.
    :type aliases: bool

    """
    return web.Response(status=200)


async def list_platforms(request: web.Request, aliases=None) -> web.Response:
    """Platform Collection

    Return a list of available platforms.

    :param aliases: Flag to display Legacy and Provider Ids.
    :type aliases: bool

    """
    return web.Response(status=200)

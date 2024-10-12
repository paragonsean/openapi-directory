from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_all_collections(request: web.Request, limit=None, offset=None, page=None) -> web.Response:
    """Get all collections

    Return&#39;s a list of all collections

    :param limit: Maximum number of results
    :type limit: int
    :param offset: Number of results to displace or skip over
    :type offset: int
    :param page: Number of results of limit length to displace or skip over
    :type page: int

    """
    return web.Response(status=200)

from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def search_get(request: web.Request, q=None) -> web.Response:
    """Search all ISBNDB databases

    Uses a free query string compatible with ElasticSearch 6 to search in any of the ISBNDB&#39;s databases

    :param q: A query string compatible with ElasticSearch 6
    :type q: str

    """
    return web.Response(status=200)

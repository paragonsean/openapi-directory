from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def search(request: web.Request, namespace, q, type=None, limit=None, offset=None) -> web.Response:
    """Get a search results

    

    :param namespace: User or team name.
    :type namespace: str
    :param q: Search string.
    :type q: str
    :param type: Limit results to specific types.
    :type type: str
    :param limit: Limit data when getting items.
    :type limit: str
    :param offset: Offset data when getting items.
    :type offset: str

    """
    return web.Response(status=200)

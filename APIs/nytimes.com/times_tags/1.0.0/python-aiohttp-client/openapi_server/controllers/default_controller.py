from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def timestags_get(request: web.Request, query, filter=None, max=None) -> web.Response:
    """timestags_get

    

    :param query: Your search query
    :type query: str
    :param filter: If you do not specify a value for filter (see the Optional Parameters), your query will be matched to tags in all four Times dictionaries: subject, geographic location, organization and person. To use more than one, separate with commas. 
    :type filter: str
    :param max: Sets the maximum number of results
    :type max: int

    """
    return web.Response(status=200)

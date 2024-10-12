from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def movies_search_search(request: web.Request, q=None, page_limit=None, page=None) -> web.Response:
    """movies_search_search

    

    :param q: The plain text search query to search for a movie. Remember to URI encode this!
    :type q: str
    :param page_limit: The amount of movie search results to show per page
    :type page_limit: str
    :param page: The selected page of movie search results
    :type page: str

    """
    return web.Response(status=200)

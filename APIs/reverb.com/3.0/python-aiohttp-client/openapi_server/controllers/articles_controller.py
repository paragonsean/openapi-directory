from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def articles_categories_get(request: web.Request, ) -> web.Response:
    """List of all article categories

    List of all article categories


    """
    return web.Response(status=200)


async def articles_get(request: web.Request, page=None, per_page=None, offset=None, query=None, exclude_featured=None) -> web.Response:
    """articles_get

    

    :param page: 
    :type page: int
    :param per_page: 
    :type per_page: int
    :param offset: 
    :type offset: int
    :param query: What&#39;s being searched for
    :type query: str
    :param exclude_featured: Number of featured articles to exclude
    :type exclude_featured: int

    """
    return web.Response(status=200)

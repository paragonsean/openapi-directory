from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_pages200_response import GetPages200Response
from openapi_server.models.get_pages200_response_pages_inner import GetPages200ResponsePagesInner
from openapi_server import util


async def get_page(request: web.Request, slug) -> web.Response:
    """get_page

    A single page&#39;s metadata from this portal 

    :param slug: Page slug. 
    :type slug: str

    """
    return web.Response(status=200)


async def get_pages(request: web.Request, ) -> web.Response:
    """get_pages

    List of all pages from this portal. 


    """
    return web.Response(status=200)

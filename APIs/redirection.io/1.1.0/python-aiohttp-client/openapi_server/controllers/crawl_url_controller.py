from typing import List, Dict
from aiohttp import web

from openapi_server.models.crawl_url_read import CrawlUrlRead
from openapi_server import util


async def get_crawl_url_collection(request: web.Request, page=None) -> web.Response:
    """Retrieves the collection of CrawlUrl resources.

    

    :param page: The collection page number
    :type page: int

    """
    return web.Response(status=200)


async def get_crawl_url_item(request: web.Request, id) -> web.Response:
    """Retrieves a CrawlUrl resource.

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)

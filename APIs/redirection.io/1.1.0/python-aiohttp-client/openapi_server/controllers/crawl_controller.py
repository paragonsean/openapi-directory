from typing import List, Dict
from aiohttp import web

from openapi_server.models.crawl import Crawl
from openapi_server.models.crawl_read import CrawlRead
from openapi_server.models.crawl_read_details import CrawlReadDetails
from openapi_server.models.crawl_write import CrawlWrite
from openapi_server import util


async def cancel_crawl_item(request: web.Request, id, crawl=None) -> web.Response:
    """Creates a Crawl resource.

    

    :param id: 
    :type id: str
    :param crawl: The new Crawl resource
    :type crawl: dict | bytes

    """
    crawl = Crawl.from_dict(crawl)
    return web.Response(status=200)


async def get_crawl_collection(request: web.Request, project_id, first_url=None, sort_created_at=None, page=None) -> web.Response:
    """Retrieves the collection of Crawl resources.

    

    :param project_id: 
    :type project_id: str
    :param first_url: 
    :type first_url: str
    :param sort_created_at: 
    :type sort_created_at: str
    :param page: The collection page number
    :type page: int

    """
    return web.Response(status=200)


async def get_crawl_item(request: web.Request, id) -> web.Response:
    """Retrieves a Crawl resource.

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def post_crawl_collection(request: web.Request, crawl=None) -> web.Response:
    """Creates a Crawl resource.

    

    :param crawl: The new Crawl resource
    :type crawl: dict | bytes

    """
    crawl = CrawlWrite.from_dict(crawl)
    return web.Response(status=200)

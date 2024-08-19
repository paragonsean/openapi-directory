from typing import List, Dict
from aiohttp import web

from openapi_server.models.publisher_single import PublisherSingle
from openapi_server.models.publishers_list200_response import PublishersList200Response
from openapi_server import util


async def publishers_list(request: web.Request, page=None, page_size=None) -> web.Response:
    """Get a list of video game publishers.

    

    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int

    """
    return web.Response(status=200)


async def publishers_read(request: web.Request, id) -> web.Response:
    """Get details of the publisher.

    

    :param id: A unique integer value identifying this Publisher.
    :type id: int

    """
    return web.Response(status=200)

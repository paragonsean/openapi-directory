from typing import List, Dict
from aiohttp import web

from openapi_server.models.developer_single import DeveloperSingle
from openapi_server.models.developers_list200_response import DevelopersList200Response
from openapi_server import util


async def developers_list(request: web.Request, page=None, page_size=None) -> web.Response:
    """Get a list of game developers.

    

    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int

    """
    return web.Response(status=200)


async def developers_read(request: web.Request, id) -> web.Response:
    """Get details of the developer.

    

    :param id: A unique integer value identifying this Developer.
    :type id: int

    """
    return web.Response(status=200)

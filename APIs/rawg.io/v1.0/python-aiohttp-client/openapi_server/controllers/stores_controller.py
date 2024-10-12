from typing import List, Dict
from aiohttp import web

from openapi_server.models.store_single import StoreSingle
from openapi_server.models.stores_list200_response import StoresList200Response
from openapi_server import util


async def stores_list(request: web.Request, ordering=None, page=None, page_size=None) -> web.Response:
    """Get a list of video game storefronts.

    

    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int

    """
    return web.Response(status=200)


async def stores_read(request: web.Request, id) -> web.Response:
    """Get details of the store.

    

    :param id: A unique integer value identifying this Store.
    :type id: int

    """
    return web.Response(status=200)

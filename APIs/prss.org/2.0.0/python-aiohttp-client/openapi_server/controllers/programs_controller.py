from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.program import Program
from openapi_server import util


async def api_v2_programs_id_get(request: web.Request, id) -> web.Response:
    """Returns the program matching the given ID.

    

    :param id: The ID of the program to operate on.
    :type id: int

    """
    return web.Response(status=200)


async def api_v2_programs_search_get(request: web.Request, keywords=None, page_start=None, page_size=None) -> web.Response:
    """Optimized free-text search for programs using various filters.

    

    :param keywords: Free text search that matches against the program title or description.
    :type keywords: str
    :param page_start: The start page of the results to return. The first item is indexed at 0.
    :type page_start: int
    :param page_size: The number of items to return. Must be between 0 and 500, inclusive.
    :type page_size: int

    """
    return web.Response(status=200)

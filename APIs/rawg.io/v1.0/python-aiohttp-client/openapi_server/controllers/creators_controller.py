from typing import List, Dict
from aiohttp import web

from openapi_server.models.creators_list200_response import CreatorsList200Response
from openapi_server.models.person_single import PersonSingle
from openapi_server import util


async def creators_list(request: web.Request, page=None, page_size=None) -> web.Response:
    """Get a list of game creators.

    

    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int

    """
    return web.Response(status=200)


async def creators_read(request: web.Request, id) -> web.Response:
    """Get details of the creator.

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)

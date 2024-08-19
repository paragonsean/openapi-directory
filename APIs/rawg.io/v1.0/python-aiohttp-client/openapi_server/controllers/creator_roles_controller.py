from typing import List, Dict
from aiohttp import web

from openapi_server.models.creator_roles_list200_response import CreatorRolesList200Response
from openapi_server import util


async def creator_roles_list(request: web.Request, page=None, page_size=None) -> web.Response:
    """Get a list of creator positions (jobs).

    

    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int

    """
    return web.Response(status=200)

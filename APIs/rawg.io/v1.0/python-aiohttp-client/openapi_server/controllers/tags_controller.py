from typing import List, Dict
from aiohttp import web

from openapi_server.models.tag_single import TagSingle
from openapi_server.models.tags_list200_response import TagsList200Response
from openapi_server import util


async def tags_list(request: web.Request, page=None, page_size=None) -> web.Response:
    """Get a list of tags.

    

    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int

    """
    return web.Response(status=200)


async def tags_read(request: web.Request, id) -> web.Response:
    """Get details of the tag.

    

    :param id: A unique integer value identifying this Tag.
    :type id: int

    """
    return web.Response(status=200)

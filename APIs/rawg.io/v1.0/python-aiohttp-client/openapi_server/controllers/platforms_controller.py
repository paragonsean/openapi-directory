from typing import List, Dict
from aiohttp import web

from openapi_server.models.platform_single import PlatformSingle
from openapi_server.models.platforms_list200_response import PlatformsList200Response
from openapi_server.models.platforms_lists_parents_list200_response import PlatformsListsParentsList200Response
from openapi_server import util


async def platforms_list(request: web.Request, ordering=None, page=None, page_size=None) -> web.Response:
    """Get a list of video game platforms.

    

    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int

    """
    return web.Response(status=200)


async def platforms_lists_parents_list(request: web.Request, ordering=None, page=None, page_size=None) -> web.Response:
    """Get a list of parent platforms.

    For instance, for PS2 and PS4 the “parent platform” is PlayStation.

    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int

    """
    return web.Response(status=200)


async def platforms_read(request: web.Request, id) -> web.Response:
    """Get details of the platform.

    

    :param id: A unique integer value identifying this Platform.
    :type id: int

    """
    return web.Response(status=200)

from typing import List, Dict
from aiohttp import web

from openapi_server.models.followed_tag import FollowedTag
from openapi_server.models.tag import Tag
from openapi_server import util


async def get_followed_tags_0(request: web.Request, ) -> web.Response:
    """Followed Tags

    This endpoint allows the client to retrieve a list of the tags they follow.


    """
    return web.Response(status=200)


async def get_tags(request: web.Request, page=None, per_page=None) -> web.Response:
    """Tags

    This endpoint allows the client to retrieve a list of tags that can be used to tag articles.  It will return tags ordered by popularity.  It supports pagination, each page will contain 10 tags by default.

    :param page: Pagination page
    :type page: int
    :param per_page: Page size (the number of items to return per page). The default maximum value can be overridden by \&quot;API_PER_PAGE_MAX\&quot; environment variable.
    :type per_page: int

    """
    return web.Response(status=200)

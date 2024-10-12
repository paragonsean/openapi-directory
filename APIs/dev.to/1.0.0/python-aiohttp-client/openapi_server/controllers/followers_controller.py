from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_followers200_response_inner import GetFollowers200ResponseInner
from openapi_server import util


async def get_followers(request: web.Request, page=None, per_page=None, sort=None) -> web.Response:
    """Followers

    This endpoint allows the client to retrieve a list of the followers they have.         \&quot;Followers\&quot; are users that are following other users on the website.         It supports pagination, each page will contain 80 followers by default.

    :param page: Pagination page
    :type page: int
    :param per_page: Page size (the number of items to return per page). The default maximum value can be overridden by \&quot;API_PER_PAGE_MAX\&quot; environment variable.
    :type per_page: int
    :param sort: Default is &#39;created_at&#39;. Specifies the sort order for the created_at param of the follow                                 relationship. To sort by newest followers first (descending order) specify                                 ?sort&#x3D;-created_at.
    :type sort: str

    """
    return web.Response(status=200)

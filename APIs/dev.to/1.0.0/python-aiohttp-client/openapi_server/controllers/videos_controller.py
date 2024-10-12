from typing import List, Dict
from aiohttp import web

from openapi_server.models.video_article import VideoArticle
from openapi_server import util


async def videos(request: web.Request, page=None, per_page=None) -> web.Response:
    """Articles with a video

    This endpoint allows the client to retrieve a list of articles that are uploaded with a video.  It will only return published video articles ordered by descending popularity.  It supports pagination, each page will contain 24 articles by default.

    :param page: Pagination page
    :type page: int
    :param per_page: Page size (the number of items to return per page). The default maximum value can be overridden by \&quot;API_PER_PAGE_MAX\&quot; environment variable.
    :type per_page: int

    """
    return web.Response(status=200)

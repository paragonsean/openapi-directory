from typing import List, Dict
from aiohttp import web

from openapi_server.models.activity31 import Activity31
from openapi_server import util


async def get_feed(request: web.Request, user_id, offset=None, page=None, per_page=None, type=None) -> web.Response:
    """Get all videos in a user&#39;s feed

    

    :param user_id: The ID of the user.
    :type user_id: 
    :param offset: Necessary for proper pagination. You shouldn&#39;t provide this value yourself, and instead use the pagination links in the feed response. Please see our [pagination documentation](https://developer.vimeo.com/api/common-formats#using-the-pagination-parameter) for more information.
    :type offset: str
    :param page: The page number of the results to show.
    :type page: 
    :param per_page: The number of items to show on each page of results, up to a maximum of 100.
    :type per_page: 
    :param type: The feed type.
    :type type: str

    """
    return web.Response(status=200)


async def get_feed_alt1(request: web.Request, offset=None, page=None, per_page=None, type=None) -> web.Response:
    """Get all videos in a user&#39;s feed

    

    :param offset: Necessary for proper pagination. You shouldn&#39;t provide this value yourself, and instead use the pagination links in the feed response. Please see our [pagination documentation](https://developer.vimeo.com/api/common-formats#using-the-pagination-parameter) for more information.
    :type offset: str
    :param page: The page number of the results to show.
    :type page: 
    :param per_page: The number of items to show on each page of results, up to a maximum of 100.
    :type per_page: 
    :param type: The feed type.
    :type type: str

    """
    return web.Response(status=200)

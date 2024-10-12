from typing import List, Dict
from aiohttp import web

from openapi_server.models.category import Category
from openapi_server.models.legacy_error import LegacyError
from openapi_server.models.suggest_video_category_request import SuggestVideoCategoryRequest
from openapi_server.models.video import Video
from openapi_server import util


async def check_category_for_video(request: web.Request, category, video_id) -> web.Response:
    """Check for a video in a category

    

    :param category: The name of the category.
    :type category: str
    :param video_id: The ID of the video.
    :type video_id: 

    """
    return web.Response(status=200)


async def get_category_videos(request: web.Request, category, direction=None, filter=None, filter_embeddable=None, page=None, per_page=None, query=None, sort=None) -> web.Response:
    """Get all the videos in a category

    

    :param category: The name of the category.
    :type category: str
    :param direction: The sort direction of the results.
    :type direction: str
    :param filter: The attribute by which to filter the results.  Option descriptions:  * &#x60;conditional_featured&#x60; - Featured (promoted) videos 
    :type filter: str
    :param filter_embeddable: Whether to filter the results by embeddable videos (&#x60;true&#x60;) or non-embeddable videos (&#x60;false&#x60;). Required only if **filter** is &#x60;embeddable&#x60;.
    :type filter_embeddable: bool
    :param page: The page number of the results to show.
    :type page: 
    :param per_page: The number of items to show on each page of results, up to a maximum of 100.
    :type per_page: 
    :param query: The search query to use to filter the results.
    :type query: str
    :param sort: The way to sort the results.
    :type sort: str

    """
    return web.Response(status=200)


async def get_video_categories(request: web.Request, video_id) -> web.Response:
    """Get all the categories to which a video belongs

    

    :param video_id: The ID of the video.
    :type video_id: 

    """
    return web.Response(status=200)


async def suggest_video_category(request: web.Request, video_id, body) -> web.Response:
    """Suggest categories for a video

    With this method, you can suggest up to two categories and one subcategory for a video. Vimeo makes the final determination about whether the video belongs in these categories.

    :param video_id: The ID of the video.
    :type video_id: 
    :param body: 
    :type body: dict | bytes

    """
    body = SuggestVideoCategoryRequest.from_dict(body)
    return web.Response(status=200)

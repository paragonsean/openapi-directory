from typing import List, Dict
from aiohttp import web

from openapi_server.models.legacy_error import LegacyError
from openapi_server.models.user import User
from openapi_server.models.video import Video
from openapi_server import util


async def check_if_user_liked_video(request: web.Request, user_id, video_id) -> web.Response:
    """Check if a user has liked a video

    

    :param user_id: The ID of the user.
    :type user_id: 
    :param video_id: The ID of the video.
    :type video_id: 

    """
    return web.Response(status=200)


async def check_if_user_liked_video_alt1(request: web.Request, video_id) -> web.Response:
    """Check if a user has liked a video

    

    :param video_id: The ID of the video.
    :type video_id: 

    """
    return web.Response(status=200)


async def get_likes(request: web.Request, user_id, filter=None, filter_embeddable=None, page=None, per_page=None, query=None, sort=None) -> web.Response:
    """Get all the videos that a user has liked

    

    :param user_id: The ID of the user.
    :type user_id: 
    :param filter: The attribute by which to filter the results.
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


async def get_likes_alt1(request: web.Request, filter=None, filter_embeddable=None, page=None, per_page=None, query=None, sort=None) -> web.Response:
    """Get all the videos that a user has liked

    

    :param filter: The attribute by which to filter the results.
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


async def get_video_likes(request: web.Request, video_id, direction=None, page=None, per_page=None, sort=None) -> web.Response:
    """Get all the users who have liked a video

    

    :param video_id: The ID of the video.
    :type video_id: 
    :param direction: The sort direction of the results.
    :type direction: str
    :param page: The page number of the results to show.
    :type page: 
    :param per_page: The number of items to show on each page of results, up to a maximum of 100.
    :type per_page: 
    :param sort: The way to sort the results.
    :type sort: str

    """
    return web.Response(status=200)


async def get_video_likes_alt1(request: web.Request, channel_id, video_id, direction=None, page=None, per_page=None, sort=None) -> web.Response:
    """Get all the users who have liked a video

    

    :param channel_id: The ID of the channel.
    :type channel_id: 
    :param video_id: The ID of the video.
    :type video_id: 
    :param direction: The sort direction of the results.
    :type direction: str
    :param page: The page number of the results to show.
    :type page: 
    :param per_page: The number of items to show on each page of results, up to a maximum of 100.
    :type per_page: 
    :param sort: The way to sort the results.
    :type sort: str

    """
    return web.Response(status=200)


async def get_vod_likes(request: web.Request, ondemand_id, direction=None, filter=None, page=None, per_page=None, sort=None) -> web.Response:
    """Get all the users who have liked a video on an On Demand page

    This method gets all the users who have liked a particular video on an On Demand page.

    :param ondemand_id: The ID of the On Demand page.
    :type ondemand_id: 
    :param direction: The sort direction of the results.
    :type direction: str
    :param filter: The attribute by which to filter the results.
    :type filter: str
    :param page: The page number of the results to show.
    :type page: 
    :param per_page: The number of items to show on each page of results, up to a maximum of 100.
    :type per_page: 
    :param sort: The way to sort the results.
    :type sort: str

    """
    return web.Response(status=200)


async def like_video(request: web.Request, user_id, video_id) -> web.Response:
    """Cause a user to like a video

    

    :param user_id: The ID of the user.
    :type user_id: 
    :param video_id: The ID of the video.
    :type video_id: 

    """
    return web.Response(status=200)


async def like_video_alt1(request: web.Request, video_id) -> web.Response:
    """Cause a user to like a video

    

    :param video_id: The ID of the video.
    :type video_id: 

    """
    return web.Response(status=200)


async def unlike_video(request: web.Request, user_id, video_id) -> web.Response:
    """Cause a user to unlike a video

    

    :param user_id: The ID of the user.
    :type user_id: 
    :param video_id: The ID of the video.
    :type video_id: 

    """
    return web.Response(status=200)


async def unlike_video_alt1(request: web.Request, video_id) -> web.Response:
    """Cause a user to unlike a video

    

    :param video_id: The ID of the video.
    :type video_id: 

    """
    return web.Response(status=200)

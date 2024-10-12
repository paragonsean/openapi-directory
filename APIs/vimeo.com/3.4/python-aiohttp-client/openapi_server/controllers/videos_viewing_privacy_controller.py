from typing import List, Dict
from aiohttp import web

from openapi_server.models.legacy_error import LegacyError
from openapi_server.models.user import User
from openapi_server import util


async def add_video_privacy_user(request: web.Request, user_id, video_id) -> web.Response:
    """Permit a specific user to view a private video

    

    :param user_id: The ID of the user.
    :type user_id: 
    :param video_id: The ID of the video.
    :type video_id: 

    """
    return web.Response(status=200)


async def add_video_privacy_users(request: web.Request, video_id) -> web.Response:
    """Permit a list of users to view a private video

    The body of this request should follow our [batch request format](https://developer.vimeo.com/api/common-formats#batch-requests). Each object must contain a single &#x60;URI&#x60; field, and the value of this field must be the URI of the user who can view this video.

    :param video_id: The ID of the video.
    :type video_id: 

    """
    return web.Response(status=200)


async def add_video_privacy_users_alt1(request: web.Request, channel_id, video_id) -> web.Response:
    """Permit a list of users to view a private video

    The body of this request should follow our [batch request format](https://developer.vimeo.com/api/common-formats#batch-requests). Each object must contain a single &#x60;URI&#x60; field, and the value of this field must be the URI of the user who can view this video.

    :param channel_id: The ID of the channel.
    :type channel_id: 
    :param video_id: The ID of the video.
    :type video_id: 

    """
    return web.Response(status=200)


async def delete_video_privacy_user(request: web.Request, user_id, video_id) -> web.Response:
    """Restrict a user from viewing a private video

    

    :param user_id: The ID of the user.
    :type user_id: 
    :param video_id: The ID of the video.
    :type video_id: 

    """
    return web.Response(status=200)


async def get_video_privacy_users(request: web.Request, video_id, page=None, per_page=None) -> web.Response:
    """Get all the users who can view a user&#39;s private videos by default

    

    :param video_id: The ID of the video.
    :type video_id: 
    :param page: The page number of the results to show.
    :type page: 
    :param per_page: The number of items to show on each page of results, up to a maximum of 100.
    :type per_page: 

    """
    return web.Response(status=200)


async def get_video_privacy_users_alt1(request: web.Request, channel_id, video_id, page=None, per_page=None) -> web.Response:
    """Get all the users who can view a user&#39;s private videos by default

    

    :param channel_id: The ID of the channel.
    :type channel_id: 
    :param video_id: The ID of the video.
    :type video_id: 
    :param page: The page number of the results to show.
    :type page: 
    :param per_page: The number of items to show on each page of results, up to a maximum of 100.
    :type per_page: 

    """
    return web.Response(status=200)

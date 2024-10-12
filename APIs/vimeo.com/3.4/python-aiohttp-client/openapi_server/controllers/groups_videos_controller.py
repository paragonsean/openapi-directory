from typing import List, Dict
from aiohttp import web

from openapi_server.models.legacy_error import LegacyError
from openapi_server.models.video import Video
from openapi_server import util


async def add_video_to_group(request: web.Request, group_id, video_id) -> web.Response:
    """Add a video to a group

    

    :param group_id: The ID of the group.
    :type group_id: 
    :param video_id: The ID of the video.
    :type video_id: 

    """
    return web.Response(status=200)


async def delete_video_from_group(request: web.Request, group_id, video_id) -> web.Response:
    """Remove a video from a group

    

    :param group_id: The ID of the group.
    :type group_id: 
    :param video_id: The ID of the video.
    :type video_id: 

    """
    return web.Response(status=200)


async def get_group_video(request: web.Request, group_id, video_id) -> web.Response:
    """Get a specific video in a group

    Check if a group has a video.

    :param group_id: The ID of the group.
    :type group_id: 
    :param video_id: The ID of the video.
    :type video_id: 

    """
    return web.Response(status=200)


async def get_group_videos(request: web.Request, group_id, direction=None, filter=None, filter_embeddable=None, page=None, per_page=None, query=None, sort=None) -> web.Response:
    """Get all the videos in a group

    

    :param group_id: The ID of the group.
    :type group_id: 
    :param direction: The sort direction of the results.
    :type direction: str
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

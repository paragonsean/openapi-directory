from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_videos_to_channel_request import AddVideosToChannelRequest
from openapi_server.models.channel import Channel
from openapi_server.models.legacy_error import LegacyError
from openapi_server.models.remove_videos_from_channel_request import RemoveVideosFromChannelRequest
from openapi_server.models.video import Video
from openapi_server import util


async def add_video_to_channel(request: web.Request, channel_id, video_id) -> web.Response:
    """Add a specific video to a channel

    

    :param channel_id: The ID of the channel.
    :type channel_id: 
    :param video_id: The ID of the video.
    :type video_id: 

    """
    return web.Response(status=200)


async def add_videos_to_channel(request: web.Request, channel_id, body) -> web.Response:
    """Add a list of videos to a channel

    

    :param channel_id: The ID of the channel.
    :type channel_id: 
    :param body: 
    :type body: dict | bytes

    """
    body = AddVideosToChannelRequest.from_dict(body)
    return web.Response(status=200)


async def delete_video_from_channel(request: web.Request, channel_id, video_id) -> web.Response:
    """Remove a specific video from a channel

    

    :param channel_id: The ID of the channel.
    :type channel_id: 
    :param video_id: The ID of the video.
    :type video_id: 

    """
    return web.Response(status=200)


async def get_available_video_channels(request: web.Request, video_id) -> web.Response:
    """Get all the channels to which a user can add or remove a specific video

    

    :param video_id: The ID of the video.
    :type video_id: 

    """
    return web.Response(status=200)


async def get_channel_video(request: web.Request, channel_id, video_id) -> web.Response:
    """Get a specific video in a channel

    This method returns a specific video in a channel. You can use it to determine whether the video is in the channel.

    :param channel_id: The ID of the channel.
    :type channel_id: 
    :param video_id: The ID of the video.
    :type video_id: 

    """
    return web.Response(status=200)


async def get_channel_videos(request: web.Request, channel_id, containing_uri=None, direction=None, filter=None, filter_embeddable=None, page=None, per_page=None, query=None, sort=None) -> web.Response:
    """Get all the videos in a channel

    

    :param channel_id: The ID of the channel.
    :type channel_id: 
    :param containing_uri: The page that contains the video URI.
    :type containing_uri: str
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


async def remove_videos_from_channel(request: web.Request, channel_id, body) -> web.Response:
    """Remove a list of videos from a channel

    

    :param channel_id: The ID of the channel.
    :type channel_id: 
    :param body: 
    :type body: dict | bytes

    """
    body = RemoveVideosFromChannelRequest.from_dict(body)
    return web.Response(status=200)

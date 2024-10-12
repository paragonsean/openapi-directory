from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_video_thumbnail_alt1_request import CreateVideoThumbnailAlt1Request
from openapi_server.models.edit_video_thumbnail_request import EditVideoThumbnailRequest
from openapi_server.models.picture import Picture
from openapi_server import util


async def create_video_thumbnail(request: web.Request, video_id, body=None) -> web.Response:
    """Add a video thumbnail

    

    :param video_id: The ID of the video.
    :type video_id: 
    :param body: 
    :type body: dict | bytes

    """
    body = CreateVideoThumbnailAlt1Request.from_dict(body)
    return web.Response(status=200)


async def create_video_thumbnail_alt1(request: web.Request, channel_id, video_id, body=None) -> web.Response:
    """Add a video thumbnail

    

    :param channel_id: The ID of the channel.
    :type channel_id: 
    :param video_id: The ID of the video.
    :type video_id: 
    :param body: 
    :type body: dict | bytes

    """
    body = CreateVideoThumbnailAlt1Request.from_dict(body)
    return web.Response(status=200)


async def delete_video_thumbnail(request: web.Request, picture_id, video_id) -> web.Response:
    """Delete a video thumbnail

    

    :param picture_id: The ID of the picture.
    :type picture_id: 
    :param video_id: The ID of the video.
    :type video_id: 

    """
    return web.Response(status=200)


async def edit_video_thumbnail(request: web.Request, picture_id, video_id, body=None) -> web.Response:
    """Edit a video thumbnail

    

    :param picture_id: The ID of the picture.
    :type picture_id: 
    :param video_id: The ID of the video.
    :type video_id: 
    :param body: 
    :type body: dict | bytes

    """
    body = EditVideoThumbnailRequest.from_dict(body)
    return web.Response(status=200)


async def get_video_thumbnail(request: web.Request, picture_id, video_id) -> web.Response:
    """Get a video thumbnail

    

    :param picture_id: The ID of the picture.
    :type picture_id: 
    :param video_id: The ID of the video.
    :type video_id: 

    """
    return web.Response(status=200)


async def get_video_thumbnails(request: web.Request, video_id, page=None, per_page=None) -> web.Response:
    """Get all the thumbnails of a video

    

    :param video_id: The ID of the video.
    :type video_id: 
    :param page: The page number of the results to show.
    :type page: 
    :param per_page: The number of items to show on each page of results, up to a maximum of 100.
    :type per_page: 

    """
    return web.Response(status=200)


async def get_video_thumbnails_alt1(request: web.Request, channel_id, video_id, page=None, per_page=None) -> web.Response:
    """Get all the thumbnails of a video

    

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

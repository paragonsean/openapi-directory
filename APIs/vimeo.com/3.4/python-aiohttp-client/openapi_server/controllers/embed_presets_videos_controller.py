from typing import List, Dict
from aiohttp import web

from openapi_server.models.legacy_error import LegacyError
from openapi_server.models.picture import Picture
from openapi_server.models.video import Video
from openapi_server import util


async def add_video_embed_preset(request: web.Request, preset_id, video_id) -> web.Response:
    """Add an embed preset to a video

    

    :param preset_id: The ID of the preset.
    :type preset_id: 
    :param video_id: The ID of the video.
    :type video_id: 

    """
    return web.Response(status=200)


async def create_video_custom_logo(request: web.Request, video_id) -> web.Response:
    """Add a new custom logo to a video

    

    :param video_id: The ID of the video.
    :type video_id: 

    """
    return web.Response(status=200)


async def delete_video_embed_preset(request: web.Request, preset_id, video_id) -> web.Response:
    """Remove an embed preset from a video

    

    :param preset_id: The ID of the preset.
    :type preset_id: 
    :param video_id: The ID of the video.
    :type video_id: 

    """
    return web.Response(status=200)


async def get_embed_preset_videos(request: web.Request, preset_id, user_id, page=None, per_page=None) -> web.Response:
    """Get all the videos that have been added to an embed preset

    

    :param preset_id: The ID of the preset.
    :type preset_id: 
    :param user_id: The ID of the user.
    :type user_id: 
    :param page: The page number of the results to show.
    :type page: 
    :param per_page: The number of items to show on each page of results, up to a maximum of 100.
    :type per_page: 

    """
    return web.Response(status=200)


async def get_embed_preset_videos_alt1(request: web.Request, preset_id, page=None, per_page=None) -> web.Response:
    """Get all the videos that have been added to an embed preset

    

    :param preset_id: The ID of the preset.
    :type preset_id: 
    :param page: The page number of the results to show.
    :type page: 
    :param per_page: The number of items to show on each page of results, up to a maximum of 100.
    :type per_page: 

    """
    return web.Response(status=200)


async def get_video_custom_logo(request: web.Request, thumbnail_id, video_id) -> web.Response:
    """Get a custom video logo

    

    :param thumbnail_id: The ID of the picture.
    :type thumbnail_id: 
    :param video_id: The ID of the video.
    :type video_id: 

    """
    return web.Response(status=200)


async def get_video_embed_preset(request: web.Request, preset_id, video_id) -> web.Response:
    """Check if an embed preset has been added to a video

    

    :param preset_id: The ID of the preset.
    :type preset_id: 
    :param video_id: The ID of the video.
    :type video_id: 

    """
    return web.Response(status=200)

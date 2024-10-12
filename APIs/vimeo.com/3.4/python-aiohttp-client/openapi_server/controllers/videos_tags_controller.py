from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_video_tags_request import AddVideoTagsRequest
from openapi_server.models.legacy_error import LegacyError
from openapi_server.models.tag import Tag
from openapi_server.models.video import Video
from openapi_server import util


async def add_video_tag(request: web.Request, video_id, word) -> web.Response:
    """Add a specific tag to a video

    

    :param video_id: The ID of the video.
    :type video_id: 
    :param word: The tag word.
    :type word: str

    """
    return web.Response(status=200)


async def add_video_tags(request: web.Request, video_id, body) -> web.Response:
    """Add a list of tags to a video

    

    :param video_id: The ID of the video.
    :type video_id: 
    :param body: 
    :type body: dict | bytes

    """
    body = AddVideoTagsRequest.from_dict(body)
    return web.Response(status=200)


async def check_video_for_tag(request: web.Request, video_id, word) -> web.Response:
    """Check if a tag has been added to a video

    

    :param video_id: The ID of the video.
    :type video_id: 
    :param word: The tag word.
    :type word: str

    """
    return web.Response(status=200)


async def delete_video_tag(request: web.Request, video_id, word) -> web.Response:
    """Remove a tag from a video

    

    :param video_id: The ID of the video.
    :type video_id: 
    :param word: The tag word.
    :type word: str

    """
    return web.Response(status=200)


async def get_video_tags(request: web.Request, video_id) -> web.Response:
    """Get all the tags of a video

    

    :param video_id: The ID of the video.
    :type video_id: 

    """
    return web.Response(status=200)


async def get_videos_with_tag(request: web.Request, word, direction=None, page=None, per_page=None, sort=None) -> web.Response:
    """Get all the videos with a specific tag

    

    :param word: The tag word.
    :type word: str
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

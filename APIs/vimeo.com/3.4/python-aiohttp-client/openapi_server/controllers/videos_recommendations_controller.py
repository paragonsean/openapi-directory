from typing import List, Dict
from aiohttp import web

from openapi_server.models.legacy_error import LegacyError
from openapi_server.models.video import Video
from openapi_server import util


async def get_related_videos(request: web.Request, video_id, filter=None, page=None, per_page=None) -> web.Response:
    """Get all the related videos of a video

    

    :param video_id: The ID of the video.
    :type video_id: 
    :param filter: The attribute by which to filter the results.
    :type filter: str
    :param page: The page number of the results to show.
    :type page: 
    :param per_page: The number of items to show on each page of results, up to a maximum of 100.
    :type per_page: 

    """
    return web.Response(status=200)

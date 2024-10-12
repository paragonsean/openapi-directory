from typing import List, Dict
from aiohttp import web

from openapi_server.models.legacy_error import LegacyError
from openapi_server.models.video import Video
from openapi_server import util


async def delete_from_watch_history(request: web.Request, video_id) -> web.Response:
    """Delete a specific video from a user&#39;s watch history

    

    :param video_id: The ID of the video.
    :type video_id: 

    """
    return web.Response(status=200)


async def delete_watch_history(request: web.Request, ) -> web.Response:
    """Delete a user&#39;s watch history

    


    """
    return web.Response(status=200)


async def get_watch_history(request: web.Request, page=None, per_page=None) -> web.Response:
    """Get all the videos that a user has watched

    

    :param page: The page number of the results to show.
    :type page: 
    :param per_page: The number of items to show on each page of results, up to a maximum of 100.
    :type per_page: 

    """
    return web.Response(status=200)

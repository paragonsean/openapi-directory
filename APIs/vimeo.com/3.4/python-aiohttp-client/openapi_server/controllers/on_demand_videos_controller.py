from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_video_to_vod_request import AddVideoToVodRequest
from openapi_server.models.legacy_error import LegacyError
from openapi_server.models.on_demand_video import OnDemandVideo
from openapi_server.models.video import Video
from openapi_server import util


async def add_video_to_vod(request: web.Request, ondemand_id, video_id, body) -> web.Response:
    """Add a video to an On Demand page

    

    :param ondemand_id: The ID of the On Demand.
    :type ondemand_id: 
    :param video_id: The ID of the video.
    :type video_id: 
    :param body: 
    :type body: dict | bytes

    """
    body = AddVideoToVodRequest.from_dict(body)
    return web.Response(status=200)


async def delete_video_from_vod(request: web.Request, ondemand_id, video_id) -> web.Response:
    """Remove a video from an On Demand page

    

    :param ondemand_id: The ID of the On Demand.
    :type ondemand_id: 
    :param video_id: The ID of the video.
    :type video_id: 

    """
    return web.Response(status=200)


async def get_vod_video(request: web.Request, ondemand_id, video_id) -> web.Response:
    """Get a specific video on an On Demand page

    

    :param ondemand_id: The ID of the On Demand.
    :type ondemand_id: 
    :param video_id: The ID of the video.
    :type video_id: 

    """
    return web.Response(status=200)


async def get_vod_videos(request: web.Request, ondemand_id, direction=None, filter=None, page=None, per_page=None, sort=None) -> web.Response:
    """Get all the videos on an On Demand page

    

    :param ondemand_id: The ID of the On Demand.
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

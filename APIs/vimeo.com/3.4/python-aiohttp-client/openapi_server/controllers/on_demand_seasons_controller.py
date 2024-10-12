from typing import List, Dict
from aiohttp import web

from openapi_server.models.legacy_error import LegacyError
from openapi_server.models.on_demand_season import OnDemandSeason
from openapi_server.models.video import Video
from openapi_server import util


async def get_vod_season(request: web.Request, ondemand_id, season_id) -> web.Response:
    """Get a specific season on an On Demand page

    

    :param ondemand_id: The ID of the On Demand.
    :type ondemand_id: 
    :param season_id: The ID of the season.
    :type season_id: 

    """
    return web.Response(status=200)


async def get_vod_season_videos(request: web.Request, ondemand_id, season_id, filter=None, page=None, per_page=None, sort=None) -> web.Response:
    """Get all the videos in a season on an On Demand page

    

    :param ondemand_id: The ID of the On Demand.
    :type ondemand_id: 
    :param season_id: The ID of the season.
    :type season_id: 
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


async def get_vod_seasons(request: web.Request, ondemand_id, direction=None, filter=None, page=None, per_page=None, sort=None) -> web.Response:
    """Get all the seasons on an On Demand page

    

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

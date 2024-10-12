from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def visual_crossing_web_services_rest_services_weatherdata_history_get(request: web.Request, max_distance=None, short_column_names=None, end_date_time=None, aggregate_hours=None, collect_station_contributions=None, start_date_time=None, max_stations=None, allow_asynch=None, locations=None, include_normals=None, content_type=None, unit_group=None, key=None) -> web.Response:
    """Retrieves hourly or daily historical weather records.

    The weather history data is suitable for retrieving hourly or daily historical weather records.

    :param max_distance: 
    :type max_distance: str
    :param short_column_names: 
    :type short_column_names: bool
    :param end_date_time: 
    :type end_date_time: str
    :param aggregate_hours: 
    :type aggregate_hours: str
    :param collect_station_contributions: 
    :type collect_station_contributions: bool
    :param start_date_time: 
    :type start_date_time: str
    :param max_stations: 
    :type max_stations: str
    :param allow_asynch: 
    :type allow_asynch: bool
    :param locations: 
    :type locations: str
    :param include_normals: 
    :type include_normals: bool
    :param content_type: 
    :type content_type: str
    :param unit_group: 
    :type unit_group: str
    :param key: 
    :type key: str

    """
    return web.Response(status=200)

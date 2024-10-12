from typing import List, Dict
from aiohttp import web

from openapi_server.models.search_road_segments import SearchRoadSegments
from openapi_server.models.vehicle_traffic_countsfor_road_segment import VehicleTrafficCountsforRoadSegment
from openapi_server import util


async def fetch_nearest_road_segments(request: web.Request, n, latitude, longitude, x_rapid_api_key, x_rapid_api_host) -> web.Response:
    """Fetch Nearest Road Segments

    For given latitude and longitude, find &#x60;n&#x60; nearest road segments

    :param n: Number of road segments to return (between 1 and 20)
    :type n: int
    :param latitude: (Required) Search coordinate latitude
    :type latitude: float
    :param longitude: (Required) Search coordinate longitude
    :type longitude: float
    :param x_rapid_api_key: (Required) Rapid API Key. See https://rapidapi.com/idealspot-inc-idealspot-inc-default/api/idealspot-geodata
    :type x_rapid_api_key: str
    :param x_rapid_api_host: 
    :type x_rapid_api_host: str

    """
    return web.Response(status=200)


async def vehicle_traffic_countsfor_road_segment(request: web.Request, segment_id, x_rapid_api_key, x_rapid_api_host) -> web.Response:
    """Vehicle Traffic Counts for Road Segment

    Time of day, day of week, and side of street vehicle traffic counts.

    :param segment_id: (Required) Road segment ID. Fetched from Search Road Segments
    :type segment_id: int
    :param x_rapid_api_key: (Required) Rapid API Key. See https://rapidapi.com/idealspot-inc-idealspot-inc-default/api/idealspot-geodata
    :type x_rapid_api_key: str
    :param x_rapid_api_host: 
    :type x_rapid_api_host: str

    """
    return web.Response(status=200)

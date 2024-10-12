from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.travel_center import TravelCenter
from openapi_server import util


async def reisezentren_get(request: web.Request, name=None) -> web.Response:
    """Get all station infos

    Get all station infos

    :param name: A station name or part of it
    :type name: str

    """
    return web.Response(status=200)


async def reisezentren_id_get(request: web.Request, id) -> web.Response:
    """Get information about a specific station

    Get information about a specific station

    :param id: Station id
    :type id: str

    """
    return web.Response(status=200)


async def reisezentren_loc_lat_lon_dist_get(request: web.Request, lat, lon, dist) -> web.Response:
    """Get stations in a given radius

    Get stations in a given radius

    :param lat: Latitude
    :type lat: float
    :param lon: Longitude
    :type lon: float
    :param dist: Radius
    :type dist: float

    """
    return web.Response(status=200)


async def reisezentren_loc_lat_lon_get(request: web.Request, lat, lon) -> web.Response:
    """Get information about a station near a location

    Get information about a station near a location

    :param lat: Latitude
    :type lat: float
    :param lon: Longitude
    :type lon: float

    """
    return web.Response(status=200)

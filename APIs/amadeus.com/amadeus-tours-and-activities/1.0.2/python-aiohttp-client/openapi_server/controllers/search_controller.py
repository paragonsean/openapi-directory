from typing import List, Dict
from aiohttp import web

from openapi_server.models.error400 import Error400
from openapi_server.models.error500 import Error500
from openapi_server.models.successful_search import SuccessfulSearch
from openapi_server import util


async def list_activities(request: web.Request, latitude, longitude, radius=None) -> web.Response:
    """Returns Activities around a given location

    

    :param latitude: Latitude (decimal coordinates)
    :type latitude: 
    :param longitude: Longitude (decimal coordinates)
    :type longitude: 
    :param radius: radius of the search in Kilometer. Can be from 0 to 20, default value is 1 Km.
    :type radius: int

    """
    return web.Response(status=200)


async def list_activities_by_square(request: web.Request, north, west, south, east) -> web.Response:
    """Returns Activities around a given location

    

    :param north: Latitude north of bounding box (decimal coordinates)
    :type north: 
    :param west: Longitude west of bounding box (decimal coordinates)
    :type west: 
    :param south: Latitude south of bounding box (decimal coordinates)
    :type south: 
    :param east: Longitude east of bounding box (decimal coordinates)
    :type east: 

    """
    return web.Response(status=200)

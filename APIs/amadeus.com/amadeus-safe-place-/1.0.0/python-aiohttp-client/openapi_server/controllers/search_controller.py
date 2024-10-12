from typing import List, Dict
from aiohttp import web

from openapi_server.models.error400 import Error400
from openapi_server.models.error500 import Error500
from openapi_server.models.success import Success
from openapi_server import util


async def get_safety_rank_by_square(request: web.Request, north, west, south, east, page_limit=None, page_offset=None) -> web.Response:
    """Returns the safety rating of a given area

    

    :param north: Latitude north of bounding box (decimal coordinates)
    :type north: float
    :param west: Longitude west of bounding box (decimal coordinates)
    :type west: float
    :param south: Latitude south of bounding box (decimal coordinates)
    :type south: float
    :param east: Longitude east of bounding box (decimal coordinates)
    :type east: float
    :param page_limit: maximum items in one page
    :type page_limit: int
    :param page_offset: start index of the requested page
    :type page_offset: int

    """
    return web.Response(status=200)


async def get_safety_ranking(request: web.Request, latitude, longitude, radius=None, page_limit=None, page_offset=None) -> web.Response:
    """Returns safety rating for a given location and radius.

    

    :param latitude: Latitude (decimal coordinates)
    :type latitude: float
    :param longitude: Longitude (decimal coordinates)
    :type longitude: float
    :param radius: radius of the search in Kilometer. Can be from 0 to 20, default value is 1 Km.
    :type radius: int
    :param page_limit: maximum items in one page
    :type page_limit: int
    :param page_offset: start index of the requested page
    :type page_offset: int

    """
    return web.Response(status=200)

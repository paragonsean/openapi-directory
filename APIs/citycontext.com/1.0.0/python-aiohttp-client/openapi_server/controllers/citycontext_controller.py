from typing import List, Dict
from aiohttp import web

from openapi_server.models.point_info import PointInfo
from openapi_server.models.usage import Usage
from openapi_server import util


async def by_point(request: web.Request, lat, lon, school_search_radius=None, park_search_radius=None) -> web.Response:
    """Query by coordinates (SRID 4326 - decimal degrees)

    

    :param lat: Latitude
    :type lat: float
    :param lon: Longitude
    :type lon: float
    :param school_search_radius: Search radius for schools, in metres, between 100 and 4000
    :type school_search_radius: int
    :param park_search_radius: Search radius for parks, in metres, between 100 and 2000
    :type park_search_radius: int

    """
    return web.Response(status=200)


async def by_postcode(request: web.Request, postcode, school_search_radius=None, park_search_radius=None) -> web.Response:
    """Query by postcode

    

    :param postcode: Postcode
    :type postcode: str
    :param school_search_radius: Search radius for schools, in metres, between 100 and 4000
    :type school_search_radius: int
    :param park_search_radius: Search radius for parks, in metres, between 100 and 2000
    :type park_search_radius: int

    """
    return web.Response(status=200)


async def usage(request: web.Request, ) -> web.Response:
    """Get usage in current month

    


    """
    return web.Response(status=200)

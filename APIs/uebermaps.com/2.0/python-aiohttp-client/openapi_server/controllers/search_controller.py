from typing import List, Dict
from aiohttp import web

from openapi_server.models.map import Map
from openapi_server.models.spot import Spot
from openapi_server.models.user import User
from openapi_server import util


async def maps_search_get(request: web.Request, q=None, d=None, lat=None, lon=None) -> web.Response:
    """Search maps

    Search maps

    :param q: Query
    :type q: str
    :param d: Distance. Diameter of search radius in meter (default: 2000 meter)
    :type d: int
    :param lat: Latitude for search radius (default distance: 2000 meter)
    :type lat: 
    :param lon: Longitude for search radius (default distance: 2000 meter)
    :type lon: 

    """
    return web.Response(status=200)


async def spots_search_get(request: web.Request, q=None, d=None, lat=None, lon=None) -> web.Response:
    """Search spots

    Search spots

    :param q: Query
    :type q: str
    :param d: Distance. Diameter of search radius in meter (default: 2000 meter)
    :type d: int
    :param lat: Latitude for search radius (2 km)
    :type lat: 
    :param lon: Longitude for search radius (2 km)
    :type lon: 

    """
    return web.Response(status=200)


async def users_search_get(request: web.Request, q=None) -> web.Response:
    """Search users

    Search users

    :param q: Query
    :type q: str

    """
    return web.Response(status=200)

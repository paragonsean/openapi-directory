from typing import List, Dict
from aiohttp import web

from openapi_server.models.place_response import PlaceResponse
from openapi_server.models.routes_response import RoutesResponse
from openapi_server import util


async def g_et_places(request: web.Request, ) -> web.Response:
    """Returns possible modes of transportation between two cities.

    


    """
    return web.Response(status=200)


async def g_et_routes(request: web.Request, origin_lat, origin_lng, destination_lat, destination_lng) -> web.Response:
    """g_et_routes

    

    :param origin_lat: 
    :type origin_lat: 
    :param origin_lng: 
    :type origin_lng: 
    :param destination_lat: 
    :type destination_lat: 
    :param destination_lng: 
    :type destination_lng: 

    """
    return web.Response(status=200)

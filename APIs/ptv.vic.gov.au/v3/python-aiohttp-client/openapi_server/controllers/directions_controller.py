from typing import List, Dict
from aiohttp import web

from openapi_server.models.v3_directions_response import V3DirectionsResponse
from openapi_server.models.v3_error_response import V3ErrorResponse
from openapi_server import util


async def directions_for_direction(request: web.Request, direction_id, token=None, devid=None, signature=None) -> web.Response:
    """View all routes for a direction of travel

    

    :param direction_id: Identifier of direction of travel; values returned by Directions API - /v3/directions/route/{route_id}
    :type direction_id: int
    :param token: Please ignore
    :type token: str
    :param devid: Your developer id
    :type devid: str
    :param signature: Authentication signature for request
    :type signature: str

    """
    return web.Response(status=200)


async def directions_for_direction_and_type(request: web.Request, direction_id, route_type, token=None, devid=None, signature=None) -> web.Response:
    """View all routes of a particular type for a direction of travel

    

    :param direction_id: Identifier of direction of travel; values returned by Directions API - /v3/directions/route/{route_id}
    :type direction_id: int
    :param route_type: Number identifying transport mode; values returned via RouteTypes API
    :type route_type: int
    :param token: Please ignore
    :type token: str
    :param devid: Your developer id
    :type devid: str
    :param signature: Authentication signature for request
    :type signature: str

    """
    return web.Response(status=200)


async def directions_for_route(request: web.Request, route_id, token=None, devid=None, signature=None) -> web.Response:
    """View directions that a route travels in

    

    :param route_id: Identifier of route; values returned by Routes API - v3/routes
    :type route_id: int
    :param token: Please ignore
    :type token: str
    :param devid: Your developer id
    :type devid: str
    :param signature: Authentication signature for request
    :type signature: str

    """
    return web.Response(status=200)

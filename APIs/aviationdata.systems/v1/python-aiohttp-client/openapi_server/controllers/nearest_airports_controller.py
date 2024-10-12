from typing import List, Dict
from aiohttp import web

from openapi_server.models.airports_api_controllers_nearest_airports_controller_response import AirportsAPIControllersNearestAirportsControllerResponse
from openapi_server import util


async def nearest_airports_nearest_airport_list(request: web.Request, result_count, latitude, longitude) -> web.Response:
    """Search for airports by location

    Required parameters: result_count, latitude, longitude, airport_service_type

    :param result_count: Required: Number of airports to return. Min: 1 Max: 20
    :type result_count: int
    :param latitude: Required: Latitude
    :type latitude: float
    :param longitude: Required: Longitude
    :type longitude: float

    """
    return web.Response(status=200)

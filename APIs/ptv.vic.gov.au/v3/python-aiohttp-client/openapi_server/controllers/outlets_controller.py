from typing import List, Dict
from aiohttp import web

from openapi_server.models.v3_error_response import V3ErrorResponse
from openapi_server.models.v3_outlet_geolocation_response import V3OutletGeolocationResponse
from openapi_server.models.v3_outlet_response import V3OutletResponse
from openapi_server import util


async def outlets_get_all_outlets(request: web.Request, max_results=None, token=None, devid=None, signature=None) -> web.Response:
    """List all ticket outlets

    

    :param max_results: Maximum number of results returned (default &#x3D; 30)
    :type max_results: int
    :param token: Please ignore
    :type token: str
    :param devid: Your developer id
    :type devid: str
    :param signature: Authentication signature for request
    :type signature: str

    """
    return web.Response(status=200)


async def outlets_get_outlets_by_geolocation(request: web.Request, latitude, longitude, max_distance=None, max_results=None, token=None, devid=None, signature=None) -> web.Response:
    """List ticket outlets near a specific location

    

    :param latitude: Geographic coordinate of latitude
    :type latitude: float
    :param longitude: Geographic coordinate of longitude
    :type longitude: float
    :param max_distance: Filter by maximum distance (in metres) from location specified via latitude and longitude parameters (default &#x3D; 300)
    :type max_distance: float
    :param max_results: Maximum number of results returned (default &#x3D; 30)
    :type max_results: int
    :param token: Please ignore
    :type token: str
    :param devid: Your developer id
    :type devid: str
    :param signature: Authentication signature for request
    :type signature: str

    """
    return web.Response(status=200)

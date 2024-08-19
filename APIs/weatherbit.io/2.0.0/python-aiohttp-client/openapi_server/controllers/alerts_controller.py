from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.weather_alert import WeatherAlert
from openapi_server import util


async def alertslatlatlonlon_get(request: web.Request, lat, lon, key, param_callback=None) -> web.Response:
    """Returns severe weather alerts issued by meteorological agencies - Given a lat/lon.

    Returns severe weather alerts issued by meteorological agencies - given a lat, and a lon.

    :param lat: Latitude component of location.
    :type lat: float
    :param lon: Longitude component of location.
    :type lon: float
    :param key: Your registered API key.
    :type key: str
    :param param_callback: Wraps return in jsonp callback - Example - callback&#x3D;func
    :type param_callback: str

    """
    return web.Response(status=200)

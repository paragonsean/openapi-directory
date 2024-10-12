from typing import List, Dict
from aiohttp import web

from openapi_server.models.forecast import Forecast
from openapi_server import util


async def get_forecast(request: web.Request, lat, lng) -> web.Response:
    """Get hourly forecasts by coordinates

    Get forecast info for the given coordinates. For every hour and property, you will get a list of weather sources and their values.

    :param lat: The latitude for a location. Valid input is a number between -90 and 90.
    :type lat: 
    :param lng: The longitude for a location. Valid input is a number between -180 and 180.
    :type lng: 

    """
    return web.Response(status=200)

from typing import List, Dict
from aiohttp import web

from openapi_server.models.anomaly import Anomaly
from openapi_server.models.height import Height
from openapi_server import util


async def app_api_egm2008_endpoints_egm2008_calculate_anomaly(request: web.Request, latitude, longitude) -> web.Response:
    """Calculate gravity anomaly values 

    for a given latitude / longitude. 

    :param latitude: Geographic latitude (-90 to 90 deg).
    :type latitude: 
    :param longitude: Geographic longitude (-180 to 180 deg).
    :type longitude: 

    """
    return web.Response(status=200)


async def app_api_egm2008_endpoints_egm2008_calculate_height(request: web.Request, latitude, longitude) -> web.Response:
    """Calculate the geoid height 

    for a given latitude / longitude.  

    :param latitude: Geographic latitude (-90 to 90 deg).
    :type latitude: 
    :param longitude: Geographic longitude (-180 to 180 deg).
    :type longitude: 

    """
    return web.Response(status=200)

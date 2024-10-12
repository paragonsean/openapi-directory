from typing import List, Dict
from aiohttp import web

from openapi_server.models.app_api_wmm_endpoints_wmm_magnetic_field200_response import AppApiWmmEndpointsWMMMagneticField200Response
from openapi_server import util


async def app_api_wmm_endpoints_wmm_magnetic_field(request: web.Request, altitude, latitude, longitude, year) -> web.Response:
    """Calculate magnetic declination, inclination, total field intensity, and grid variation 

    at specified conditions. 

    :param altitude: Geodetic Altitude 0 km to 600 km.
    :type altitude: 
    :param latitude: Geodetic Latitude. -90 deg (S) to 90 deg (N).
    :type latitude: 
    :param longitude: Geodetic Longitude. -180 deg (W) to 180 deg (E).
    :type longitude: 
    :param year: Year as a decimal in the range 2015-2025 (2017.5 would be half way through 2017).
    :type year: 

    """
    return web.Response(status=200)

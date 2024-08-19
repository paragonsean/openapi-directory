from typing import List, Dict
from aiohttp import web

from openapi_server.models.app_api_endpoints_jb2008_sample_atmosphere200_response import AppApiEndpointsJB2008SampleAtmosphere200Response
from openapi_server import util


async def app_api_endpoints_jb2008_sample_atmosphere(request: web.Request, year, month, day, altitude, geodetic_latitude, geodetic_longitude, utc) -> web.Response:
    """Compute atmospheric density and temperatures 

    under given conditions. 

    :param year: Year in YYYY format
    :type year: int
    :param month: Month in MM format
    :type month: int
    :param day: Day in DD format
    :type day: int
    :param altitude: Altitude in (km)
    :type altitude: 
    :param geodetic_latitude: GeodeticLatitude (deg) -90 to 90 deg
    :type geodetic_latitude: 
    :param geodetic_longitude: GeodeticLongitude (deg) 0 to 360 deg
    :type geodetic_longitude: 
    :param utc: Coordinated Universal Time (hrs)
    :type utc: 

    """
    return web.Response(status=200)

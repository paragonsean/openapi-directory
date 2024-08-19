from typing import List, Dict
from aiohttp import web

from openapi_server.models.app_api_endpoints_nrlmsise00_sample_atmosphere200_response import AppApiEndpointsNRLMSISE00SampleAtmosphere200Response
from openapi_server import util


async def app_api_endpoints_nrlmsise00_sample_atmosphere(request: web.Request, year, month, day, altitude, geodetic_latitude, geodetic_longitude, utc, f107a=None, f107=None, ap=None) -> web.Response:
    """Compute atmospheric composition, density, and temperatures 

    at specified conditions. 

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
    :param f107a: (Optional) 81 day average of F10.7 flux (SFU) centered on the specified day. F107 and F107A values correspond to the 10.7 cm radio flux at the actual distance of Earth from Sun rather than radio flux at 1 AU. F107, F107A, AP effects can be neglected below 80 km. If unspecified, values provided by the US National Oceanic and  Atmospheric Administration are retrieved automatically. 
    :type f107a: 
    :param f107: (Optional) Daily F10.7 cm radio flux for previous day (SFU). F107 and F107A values correspond to the 10.7 cm radio flux at the actual distance of Earth from Sun rather than radio flux at 1 AU. F107, F107A, AP effects can be neglected below 80 km. If unspecified, values provided by the US National Oceanic and  Atmospheric Administration are retrieved automatically. 
    :type f107: 
    :param ap: (Optional) The Ap-index provides a daily average level for geomagnetic activity F107, F107A, AP effects can be neglected below 80 km. If unspecified, the average of values in the 24 hours preceding the date-time  are automatically calculated from data provided by GFZ German Research Centre  for Geosciences. 
    :type ap: 

    """
    return web.Response(status=200)

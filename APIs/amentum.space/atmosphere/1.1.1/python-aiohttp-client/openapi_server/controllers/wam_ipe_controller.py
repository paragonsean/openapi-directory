from typing import List, Dict
from aiohttp import web

from openapi_server.models.app_api_wfs_endpoints_wfs_get_values200_response import AppApiWfsEndpointsWFSGetValues200Response
from openapi_server import util


async def app_api_wfs_endpoints_wfs_get_values(request: web.Request, latitude, longitude, altitude, year, month, day, hour, minute) -> web.Response:
    """Forecast winds, ion and molecular densities, and temperatures in the atmosphere 

    at a given position and time on 42-48 hour forecast horizon (10 minute resolution). NOTE: latitudes outside the interval (-90,90) are clipped to the endpoints; longitudes outside (0,360) are wrapped.    

    :param latitude: Latitude (deg) -90 to 90 deg
    :type latitude: 
    :param longitude: Longitude (deg) 0 to 360 deg or -180 to 180 deg
    :type longitude: 
    :param altitude: Altitude in (km)
    :type altitude: 
    :param year: Year in YYYY format
    :type year: int
    :param month: Month in MM format
    :type month: int
    :param day: Day in DD format
    :type day: int
    :param hour: UTC Hour of the day in 24 hour format
    :type hour: int
    :param minute: Minute of the given hour
    :type minute: int

    """
    return web.Response(status=200)

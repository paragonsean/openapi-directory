from typing import List, Dict
from aiohttp import web

from openapi_server.models.aq_hourly import AQHourly
from openapi_server.models.error import Error
from openapi_server import util


async def forecast_airqualitycity_idcity_id_get(request: web.Request, city_id, key, param_callback=None, hours=None) -> web.Response:
    """Returns 72 hour (hourly) Air Quality forecast - Given a City ID.

    Returns 72 hour (hourly) Air Quality forecast, where each point represents a one hour period.

    :param city_id: City ID. Example: 4487042
    :type city_id: int
    :param key: Your registered API key.
    :type key: str
    :param param_callback: Wraps return in jsonp callback. Example - callback&#x3D;func
    :type param_callback: str
    :param hours: Number of hours to return.
    :type hours: int

    """
    return web.Response(status=200)


async def forecast_airqualitycitycitycountrycountry_get(request: web.Request, city, country, key, state=None, param_callback=None, hours=None) -> web.Response:
    """Returns 72 hour (hourly) Air Quality forecast - Given City and/or State, Country.

    Returns 72 hour (hourly) Air Quality forecast, where each point represents a one hour period.

    :param city: City search.. Example - &amp;city&#x3D;Raleigh,NC or &amp;city&#x3D;Berlin,DE or city&#x3D;Paris&amp;country&#x3D;FR
    :type city: str
    :param country: Country Code (2 letter).
    :type country: str
    :param key: Your registered API key.
    :type key: str
    :param state: Full name of state.
    :type state: str
    :param param_callback: Wraps return in jsonp callback. Example: callback&#x3D;func
    :type param_callback: str
    :param hours: Number of hours to return.
    :type hours: int

    """
    return web.Response(status=200)


async def forecast_airqualitylatlatlonlon_get(request: web.Request, lat, lon, key, param_callback=None, hours=None) -> web.Response:
    """Returns 72 hour (hourly) Air Quality forecast - Given a lat/lon.

    Returns 72 hour (hourly) Air Quality forecast, where each point represents a one hour period.

    :param lat: Latitude component of location.
    :type lat: float
    :param lon: Longitude component of location.
    :type lon: float
    :param key: Your registered API key.
    :type key: str
    :param param_callback: Wraps return in jsonp callback. Example - callback&#x3D;func
    :type param_callback: str
    :param hours: Number of hours to return.
    :type hours: int

    """
    return web.Response(status=200)


async def forecast_airqualitypostal_codepostal_code_get(request: web.Request, postal_code, key, country=None, param_callback=None, hours=None) -> web.Response:
    """Returns 72 hour (hourly) Air Quality forecast - Given a Postal Code.

    Returns 72 hour (hourly) Air Quality forecast, where each point represents a one hour period.

    :param postal_code: Postal Code. Example: 28546
    :type postal_code: int
    :param key: Your registered API key.
    :type key: str
    :param country: Country Code (2 letter).
    :type country: str
    :param param_callback: Wraps return in jsonp callback. Example - callback&#x3D;func
    :type param_callback: str
    :param hours: Number of hours to return.
    :type hours: int

    """
    return web.Response(status=200)

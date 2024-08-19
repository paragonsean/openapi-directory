from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.forecast_hourly import ForecastHourly
from openapi_server import util


async def forecast_hourlycity_idcity_id_get(request: web.Request, city_id, key, units=None, lang=None, param_callback=None, hours=None) -> web.Response:
    """Returns an hourly forecast - Given a City ID.

     Returns an hourly forecast, where each point represents a one hour   period. Every point has a datetime string in the format \&quot;YYYY-MM-DD:HH\&quot;. Time is UTC.  

    :param city_id: City ID. Example: 4487042
    :type city_id: int
    :param key: Your registered API key.
    :type key: str
    :param units: Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt;
    :type units: str
    :param lang: Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt;
    :type lang: str
    :param param_callback: Wraps return in jsonp callback. Example - callback&#x3D;func
    :type param_callback: str
    :param hours: Number of hours to return.
    :type hours: int

    """
    return web.Response(status=200)


async def forecast_hourlycitycitycountrycountry_get(request: web.Request, city, country, key, state=None, units=None, lang=None, param_callback=None, hours=None) -> web.Response:
    """Returns an hourly forecast - Given City and/or State, Country.

     Returns an hourly forecast, where each point represents a one hour   period. Every point has a datetime string in the format \&quot;YYYY-MM-DD:HH\&quot;. Time is UTC. Accepts a city in the format of City,ST or City. The state, and country parameters can be provided to make the search more accurate. 

    :param city: City search.. Example - &amp;city&#x3D;Raleigh,NC or &amp;city&#x3D;Berlin,DE or city&#x3D;Paris&amp;country&#x3D;FR
    :type city: str
    :param country: Country Code (2 letter).
    :type country: str
    :param key: Your registered API key.
    :type key: str
    :param state: Full name of state.
    :type state: str
    :param units: Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt;
    :type units: str
    :param lang: Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt;
    :type lang: str
    :param param_callback: Wraps return in jsonp callback. Example: callback&#x3D;func
    :type param_callback: str
    :param hours: Number of hours to return.
    :type hours: int

    """
    return web.Response(status=200)


async def forecast_hourlylatlatlonlon_get(request: web.Request, lat, lon, key, units=None, lang=None, param_callback=None, hours=None) -> web.Response:
    """Returns an hourly forecast - Given a lat/lon.

    Returns an hourly forecast, where each point represents a one hour period. Every point has a datetime string in the format \&quot;YYYY-MM-DD:HH\&quot;. Time is UTC.  

    :param lat: Latitude component of location.
    :type lat: float
    :param lon: Longitude component of location.
    :type lon: float
    :param key: Your registered API key.
    :type key: str
    :param units: Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt;
    :type units: str
    :param lang: Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt;
    :type lang: str
    :param param_callback: Wraps return in jsonp callback. Example - callback&#x3D;func
    :type param_callback: str
    :param hours: Number of hours to return.
    :type hours: int

    """
    return web.Response(status=200)


async def forecast_hourlypostal_codepostal_code_get(request: web.Request, postal_code, key, country=None, units=None, lang=None, param_callback=None, hours=None) -> web.Response:
    """Returns an hourly forecast - Given a Postal Code.

     Returns an hourly forecast, where each point represents a one hour   period. Every point has a datetime string in the format \&quot;YYYY-MM-DD:HH\&quot;. Time is UTC.  

    :param postal_code: Postal Code. Example: 28546
    :type postal_code: int
    :param key: Your registered API key.
    :type key: str
    :param country: Country Code (2 letter).
    :type country: str
    :param units: Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt;
    :type units: str
    :param lang: Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt;
    :type lang: str
    :param param_callback: Wraps return in jsonp callback. Example - callback&#x3D;func
    :type param_callback: str
    :param hours: Number of hours to return.
    :type hours: int

    """
    return web.Response(status=200)

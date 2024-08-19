from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.forecast_day import ForecastDay
from openapi_server import util


async def forecast_dailycity_idcity_id_get(request: web.Request, city_id, key, days=None, units=None, lang=None, param_callback=None) -> web.Response:
    """Returns a daily forecast - Given a City ID.

    Returns a daily forecast, where each point represents one day (24hr) period. Every point has a datetime string in the format \&quot;YYYY-MM-DD\&quot;. One day begins at 00:00 UTC, and ends at 23:59 UTC. 

    :param city_id: City ID. Example: 4487042
    :type city_id: int
    :param key: Your registered API key.
    :type key: str
    :param days: Number of days to return. Default 16.
    :type days: 
    :param units: Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt;
    :type units: str
    :param lang: Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt;
    :type lang: str
    :param param_callback: Wraps return in jsonp callback. Example: callback&#x3D;func
    :type param_callback: str

    """
    return web.Response(status=200)


async def forecast_dailycitycitycountrycountry_get(request: web.Request, city, country, key, state=None, days=None, units=None, lang=None, param_callback=None) -> web.Response:
    """Returns a daily forecast - Given City and/or State, Country.

    Returns a daily forecast, where each point represents one day (24hr) period. Every point has a datetime string in the format \&quot;YYYY-MM-DD\&quot;. One day begins at 00:00 UTC, and ends at 23:59 UTC. Accepts a city in the format of City,ST or City. The state, and country parameters can be provided to make the search more accurate. 

    :param city: City search.. Example - &amp;city&#x3D;Raleigh,NC or &amp;city&#x3D;Berlin,DE or city&#x3D;Paris&amp;country&#x3D;FR
    :type city: str
    :param country: Country Code (2 letter).
    :type country: str
    :param key: Your registered API key.
    :type key: str
    :param state: Full name of state.
    :type state: str
    :param days: Number of days to return. Default 16.
    :type days: 
    :param units: Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt;
    :type units: str
    :param lang: Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt;
    :type lang: str
    :param param_callback: Wraps return in jsonp callback. Example - callback&#x3D;func
    :type param_callback: str

    """
    return web.Response(status=200)


async def forecast_dailylatlatlonlon_get(request: web.Request, lat, lon, key, days=None, units=None, lang=None, param_callback=None) -> web.Response:
    """Returns a daily forecast - Given Lat/Lon.

    Returns a daily forecast, where each point represents one day (24hr) period. Every point has a datetime string in the format \&quot;YYYY-MM-DD\&quot;. One day begins at 00:00 UTC, and ends at 23:59 UTC.  

    :param lat: Latitude component of location.
    :type lat: float
    :param lon: Longitude component of location.
    :type lon: float
    :param key: Your registered API key.
    :type key: str
    :param days: Number of days to return. Default 16.
    :type days: 
    :param units: Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt;
    :type units: str
    :param lang: Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt;
    :type lang: str
    :param param_callback: Wraps return in jsonp callback. Example: callback&#x3D;func
    :type param_callback: str

    """
    return web.Response(status=200)


async def forecast_dailypostal_codepostal_code_get(request: web.Request, postal_code, key, country=None, days=None, units=None, lang=None, param_callback=None) -> web.Response:
    """Returns a daily forecast - Given a Postal Code.

    Returns a daily forecast, where each point represents one day (24hr) period. Every point has a datetime string in the format \&quot;YYYY-MM-DD\&quot;. One day begins at 00:00 UTC, and ends at 23:59 UTC. 

    :param postal_code: Postal Code. Example: 28546
    :type postal_code: int
    :param key: Your registered API key.
    :type key: str
    :param country: Country Code (2 letter).
    :type country: str
    :param days: Number of days to return. Default 16.
    :type days: 
    :param units: Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt;
    :type units: str
    :param lang: Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt;
    :type lang: str
    :param param_callback: Wraps return in jsonp callback. Example: callback&#x3D;func
    :type param_callback: str

    """
    return web.Response(status=200)

from typing import List, Dict
from aiohttp import web

from openapi_server.models.current_obs_group import CurrentObsGroup
from openapi_server.models.error import Error
from openapi_server import util


async def currentcitiescities_get(request: web.Request, cities, key, units=None, marine=None, lang=None, param_callback=None) -> web.Response:
    """Returns a group of observations given a list of cities

    Returns a group of Current Observations - Given a list of City IDs. 

    :param cities: Comma separated list of City ID&#39;s. Example: 4487042, 4494942, 4504871
    :type cities: str
    :param key: Your registered API key.
    :type key: str
    :param units: Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt;
    :type units: str
    :param marine: Marine stations only (buoys, oil platforms, etc)
    :type marine: str
    :param lang: Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt;
    :type lang: str
    :param param_callback: Wraps return in jsonp callback - Example - callback&#x3D;func
    :type param_callback: str

    """
    return web.Response(status=200)


async def currentcity_idcity_id_get(request: web.Request, city_id, key, units=None, include=None, marine=None, lang=None, param_callback=None) -> web.Response:
    """Returns a current observation by city id.

    Returns current weather observation - Given a City ID. 

    :param city_id: City ID. Example: 4487042
    :type city_id: str
    :param key: Your registered API key.
    :type key: str
    :param units: Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt;
    :type units: str
    :param include: Include 1 hour - minutely forecast in the response
    :type include: str
    :param marine: Marine stations only (buoys, oil platforms, etc)
    :type marine: str
    :param lang: Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt;
    :type lang: str
    :param param_callback: Wraps return in jsonp callback - Example - callback&#x3D;func
    :type param_callback: str

    """
    return web.Response(status=200)


async def currentcitycitycountrycountry_get(request: web.Request, city, country, key, include=None, state=None, marine=None, units=None, lang=None, param_callback=None) -> web.Response:
    """Returns a Current Observation - Given City and/or State, Country.

    Returns a Current Observation - Given a city in the format of City,ST or City. The state, and country parameters can be provided to make the search more accurate.

    :param city: City search.. Example - &amp;city&#x3D;Raleigh,NC or &amp;city&#x3D;Berlin,DE or city&#x3D;Paris&amp;country&#x3D;FR
    :type city: str
    :param country: Country Code (2 letter).
    :type country: str
    :param key: Your registered API key.
    :type key: str
    :param include: Include 1 hour - minutely forecast in the response
    :type include: str
    :param state: Full name of state.
    :type state: str
    :param marine: Marine stations only (buoys, oil platforms, etc)
    :type marine: str
    :param units: Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt;
    :type units: str
    :param lang: Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt;
    :type lang: str
    :param param_callback: Wraps return in jsonp callback - Example - callback&#x3D;func
    :type param_callback: str

    """
    return web.Response(status=200)


async def currentlatlatlonlon_get(request: web.Request, lat, lon, key, include=None, marine=None, units=None, lang=None, param_callback=None) -> web.Response:
    """Returns a Current Observation - Given a lat/lon.

    Returns a Current Observation - given a lat, and a lon.

    :param lat: Latitude component of location.
    :type lat: float
    :param lon: Longitude component of location.
    :type lon: float
    :param key: Your registered API key.
    :type key: str
    :param include: Include 1 hour - minutely forecast in the response
    :type include: str
    :param marine: Marine stations only (buoys, oil platforms, etc)
    :type marine: str
    :param units: Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt;
    :type units: str
    :param lang: Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt;
    :type lang: str
    :param param_callback: Wraps return in jsonp callback - Example - callback&#x3D;func
    :type param_callback: str

    """
    return web.Response(status=200)


async def currentpointspoints_get(request: web.Request, points, key, units=None, lang=None, param_callback=None) -> web.Response:
    """Returns a group of observations given a list of points in the format (lat1, lon1), (lat2, lon2), (latN, lonN), ...

    Returns a group of Current Observations - Given a list of points (lat1, lon1), (lat2, lon2), (latN, lonN), ...

    :param points: Comma separated list of points. Example: (35.5, -75.5),(45, 65),(45.12, -130.5)
    :type points: str
    :param key: Your registered API key.
    :type key: str
    :param units: Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt;
    :type units: str
    :param lang: Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt;
    :type lang: str
    :param param_callback: Wraps return in jsonp callback. Example: callback&#x3D;func
    :type param_callback: str

    """
    return web.Response(status=200)


async def currentpostal_codepostal_code_get(request: web.Request, postal_code, key, country=None, include=None, marine=None, units=None, lang=None, param_callback=None) -> web.Response:
    """Returns a current observation by postal code.

    Returns current weather observation - Given a Postal Code. 

    :param postal_code: Postal Code. Example: 28546
    :type postal_code: str
    :param key: Your registered API key.
    :type key: str
    :param country: Country Code (2 letter).
    :type country: str
    :param include: Include 1 hour - minutely forecast in the response
    :type include: str
    :param marine: Marine stations only (buoys, oil platforms, etc)
    :type marine: str
    :param units: Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt;
    :type units: str
    :param lang: Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt;
    :type lang: str
    :param param_callback: Wraps return in jsonp callback - Example - callback&#x3D;func
    :type param_callback: str

    """
    return web.Response(status=200)


async def currentstationsstations_get(request: web.Request, stations, key, units=None, lang=None, param_callback=None) -> web.Response:
    """Returns a group of observations given a list of stations

    Returns a group of Current Observations - Given a list of Station Call IDs. 

    :param stations: Comma separated list of Station Call ID&#39;s. Example: KRDU,KBFI,KVNY
    :type stations: str
    :param key: Your registered API key.
    :type key: str
    :param units: Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt;
    :type units: str
    :param lang: Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt;
    :type lang: str
    :param param_callback: Wraps return in jsonp callback. Example: callback&#x3D;func
    :type param_callback: str

    """
    return web.Response(status=200)


async def currentstationstation_get(request: web.Request, station, key, include=None, units=None, lang=None, param_callback=None) -> web.Response:
    """Returns a Current Observation. - Given a station ID.

    Returns a Current Observation - Given a station ID.

    :param station: Station Call ID.
    :type station: str
    :param key: Your registered API key.
    :type key: str
    :param include: Include 1 hour - minutely forecast in the response
    :type include: str
    :param units: Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt;
    :type units: str
    :param lang: Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt;
    :type lang: str
    :param param_callback: Wraps return in jsonp callback. Example: callback&#x3D;func
    :type param_callback: str

    """
    return web.Response(status=200)

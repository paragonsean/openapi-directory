from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.history import History
from openapi_server.models.history_subhourly import HistorySubhourly
from openapi_server import util


async def history_subhourlycity_idcity_id_get(request: web.Request, city_id, start_date, end_date, key, units=None, lang=None, tz=None, param_callback=None) -> web.Response:
    """Returns Historical Observations - Given a City ID

    Returns Historical Observations - Given a City ID.

    :param city_id: City ID. Example: 4487042
    :type city_id: str
    :param start_date: Start Date (YYYY-MM-DD or YYYY-MM-DD:HH)
    :type start_date: str
    :param end_date: End Date (YYYY-MM-DD or YYYY-MM-DD:HH)
    :type end_date: str
    :param key: Your registered API key.
    :type key: str
    :param units: Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt;
    :type units: str
    :param lang: Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt;
    :type lang: str
    :param tz: Assume utc (default) or local time for start_date, end_date
    :type tz: str
    :param param_callback: Wraps return in jsonp callback. Example: callback&#x3D;func
    :type param_callback: str

    """
    return web.Response(status=200)


async def history_subhourlycitycitycountrycountry_get(request: web.Request, city, country, start_date, end_date, key, state=None, units=None, lang=None, tz=None, param_callback=None) -> web.Response:
    """Returns Historical Observations - Given City and/or State, Country.

    Returns Historical Observations - Given a city in the format of City,ST or City. The state, and country parameters can be provided to make the search more accurate.

    :param city: City search. Example - &amp;city&#x3D;Raleigh,NC or &amp;city&#x3D;Berlin,DE or city&#x3D;Paris&amp;country&#x3D;FR
    :type city: str
    :param country: Country Code (2 letter).
    :type country: str
    :param start_date: Start Date (YYYY-MM-DD or YYYY-MM-DD:HH).
    :type start_date: str
    :param end_date: End Date (YYYY-MM-DD or YYYY-MM-DD:HH).
    :type end_date: str
    :param key: Your registered API key.
    :type key: str
    :param state: Full name of state.
    :type state: str
    :param units: Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt;
    :type units: str
    :param lang: Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt;
    :type lang: str
    :param tz: Assume utc (default) or local time for start_date, end_date
    :type tz: str
    :param param_callback: Wraps return in jsonp callback. Example: callback&#x3D;func
    :type param_callback: str

    """
    return web.Response(status=200)


async def history_subhourlylatlatlonlon_get(request: web.Request, lat, lon, start_date, end_date, key, units=None, lang=None, tz=None, param_callback=None) -> web.Response:
    """Returns Historical Observations - Given a lat/lon.

    Returns Historical Observations - Given a lat, and lon.

    :param lat: Latitude component of location.
    :type lat: float
    :param lon: Longitude component of location.
    :type lon: float
    :param start_date: Start Date (YYYY-MM-DD or YYYY-MM-DD:HH).
    :type start_date: str
    :param end_date: End Date (YYYY-MM-DD or YYYY-MM-DD:HH).
    :type end_date: str
    :param key: Your registered API key.
    :type key: str
    :param units: Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt;
    :type units: str
    :param lang: Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt;
    :type lang: str
    :param tz: Assume utc (default) or local time for start_date, end_date
    :type tz: str
    :param param_callback: Wraps return in jsonp callback. Example: callback&#x3D;func
    :type param_callback: str

    """
    return web.Response(status=200)


async def history_subhourlypostal_codepostal_code_get(request: web.Request, postal_code, start_date, end_date, key, country=None, units=None, lang=None, tz=None, param_callback=None) -> web.Response:
    """Returns Historical Observations - Given a Postal Code

    Returns Historical Observations - Given a Postal Code.

    :param postal_code: Postal Code. Example: 28546
    :type postal_code: str
    :param start_date: Start Date (YYYY-MM-DD or YYYY-MM-DD:HH)
    :type start_date: str
    :param end_date: End Date (YYYY-MM-DD or YYYY-MM-DD:HH)
    :type end_date: str
    :param key: Your registered API key.
    :type key: str
    :param country: Country Code (2 letter).
    :type country: str
    :param units: Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt;
    :type units: str
    :param lang: Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt;
    :type lang: str
    :param tz: Assume utc (default) or local time for start_date, end_date
    :type tz: str
    :param param_callback: Wraps return in jsonp callback. Example: callback&#x3D;func
    :type param_callback: str

    """
    return web.Response(status=200)


async def history_subhourlystationstation_get(request: web.Request, station, start_date, end_date, key, units=None, lang=None, tz=None, param_callback=None) -> web.Response:
    """Returns Historical Observations - Given a station ID.

    Returns Historical Observations - Given a station ID.

    :param station: Station ID.
    :type station: str
    :param start_date: Start Date (YYYY-MM-DD or YYYY-MM-DD:HH).
    :type start_date: str
    :param end_date: End Date (YYYY-MM-DD or YYYY-MM-DD:HH).
    :type end_date: str
    :param key: Your registered API key.
    :type key: str
    :param units: Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt;
    :type units: str
    :param lang: Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt;
    :type lang: str
    :param tz: Assume utc (default) or local time for start_date, end_date
    :type tz: str
    :param param_callback: Wraps return in jsonp callback. Example: callback&#x3D;func
    :type param_callback: str

    """
    return web.Response(status=200)

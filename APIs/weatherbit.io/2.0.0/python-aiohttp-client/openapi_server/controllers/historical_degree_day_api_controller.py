from typing import List, Dict
from aiohttp import web

from openapi_server.models.energy_obs_group import EnergyObsGroup
from openapi_server.models.error import Error
from openapi_server import util


async def history_energylatlatlonlon_get(request: web.Request, lat, lon, start_date, end_date, key, tp=None, threshold=None, units=None, param_callback=None) -> web.Response:
    """Returns Energy API response  - Given a single lat/lon. 

    Returns aggregate energy specific historical weather fields, over a specified time period.

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
    :param tp: Time period to aggregate by (daily, monthly)
    :type tp: str
    :param threshold: Temperature threshold to use to calculate degree days (default 18 C) 
    :type threshold: float
    :param units: Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt;
    :type units: str
    :param param_callback: Wraps return in jsonp callback. Example: callback&#x3D;func
    :type param_callback: str

    """
    return web.Response(status=200)

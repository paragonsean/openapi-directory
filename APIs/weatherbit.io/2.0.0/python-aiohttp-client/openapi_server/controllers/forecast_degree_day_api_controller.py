from typing import List, Dict
from aiohttp import web

from openapi_server.models.energy_obs_group_forecast import EnergyObsGroupForecast
from openapi_server.models.error import Error
from openapi_server import util


async def forecast_energylatlatlonlon_get(request: web.Request, lat, lon, key, threshold=None, units=None, tp=None, param_callback=None) -> web.Response:
    """Returns Energy Forecast API response  - Given a single lat/lon. 

    Retrieve an 8 day forecast relevant to te Energy Sector (degree days, solar radiation, precipitation, wind).

    :param lat: Latitude component of location.
    :type lat: float
    :param lon: Longitude component of location.
    :type lon: float
    :param key: Your registered API key.
    :type key: str
    :param threshold: Temperature threshold to use to calculate degree days (default 18 C) 
    :type threshold: float
    :param units: Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt;
    :type units: str
    :param tp: Time period (default: daily)
    :type tp: str
    :param param_callback: Wraps return in jsonp callback. Example: callback&#x3D;func
    :type param_callback: str

    """
    return web.Response(status=200)

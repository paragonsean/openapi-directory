from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def visual_crossing_web_services_rest_services_weatherdata_forecast_get(request: web.Request, send_as_datasource=None, allow_asynch=None, short_column_names=None, locations=None, aggregate_hours=None, content_type=None, unit_group=None, key=None) -> web.Response:
    """Weather Forecast API

    Provides access to weather forecast information. The forecast is available for up to 15 days at the hourly, 12 hour and daily summary level.

    :param send_as_datasource: 
    :type send_as_datasource: bool
    :param allow_asynch: 
    :type allow_asynch: bool
    :param short_column_names: 
    :type short_column_names: bool
    :param locations: 
    :type locations: str
    :param aggregate_hours: 
    :type aggregate_hours: str
    :param content_type: 
    :type content_type: str
    :param unit_group: 
    :type unit_group: str
    :param key: 
    :type key: str

    """
    return web.Response(status=200)

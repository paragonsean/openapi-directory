from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def visual_crossing_web_services_rest_services_timeline_location_startdate_get(request: web.Request, location, startdate, key, content_type=None, unit_group=None, include=None, lang=None) -> web.Response:
    """Historical and Forecast Weather API

    Seamless access to daily and hourly historical and forecast weather data plus weather alerts, events and current conditions.

    :param location: 
    :type location: str
    :param startdate: 
    :type startdate: str
    :param key: 
    :type key: str
    :param content_type: data format of the output either json or CSV
    :type content_type: str
    :param unit_group: 
    :type unit_group: str
    :param include: data to include in the output (required for CSV format - days,hours,alerts,current,events )
    :type include: str
    :param lang: Language to use for weather descriptions
    :type lang: str

    """
    return web.Response(status=200)

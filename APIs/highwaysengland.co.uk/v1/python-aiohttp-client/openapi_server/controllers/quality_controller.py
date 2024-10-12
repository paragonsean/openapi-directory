from typing import List, Dict
from aiohttp import web

from openapi_server.models.daily_quality_response import DailyQualityResponse
from openapi_server.models.overall_quality_response import OverallQualityResponse
from openapi_server import util


async def quality_get_daily_data_quality_for_site(request: web.Request, site_id, start_date, end_date, version) -> web.Response:
    """Get Site DailyQuality

    

    :param site_id: 
    :type site_id: str
    :param start_date: The start date of the report in the format ddmmyyyy (i.e 31012016)
    :type start_date: str
    :param end_date: The end date of the report in the format ddmmyyyy (i.e 31012016)
    :type end_date: str
    :param version: 
    :type version: str

    """
    return web.Response(status=200)


async def quality_get_overall_data_quality_for_sites(request: web.Request, sites, start_date, end_date, version) -> web.Response:
    """Get Site OverallQuality

    

    :param sites: Get site quality by site id delimited by ,
    :type sites: str
    :param start_date: The start date of the report in the format ddmmyyyy (i.e 31012016)
    :type start_date: str
    :param end_date: The end date of the report in the format ddmmyyyy (i.e 31012016)
    :type end_date: str
    :param version: 
    :type version: str

    """
    return web.Response(status=200)

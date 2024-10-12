from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def reports_sites_id_get(request: web.Request, id, _from=None, to=None, reports=None, log_type=None, compare=None) -> web.Response:
    """Returns a PDF report for a specific site

    Returns a PDF report based on a site ID

    :param id: ID that needs to be fetched
    :type id: int
    :param _from: Start of the report, format YYYY-MM-DD, default today-30day 
    :type _from: str
    :param to: End of the report, format YYYY-MM-DD, default today
    :type to: str
    :param reports: Type of reports separate by comas: Ga,Logs,Uptime
    :type reports: str
    :param log_type: Type of the log to show in the report
    :type log_type: str
    :param compare: Define if you want show previous values in Google Analytics graph
    :type compare: int

    """
    return web.Response(status=200)


async def reports_tags_id_get(request: web.Request, id, _from=None, to=None, reports=None, log_type=None, compare=None) -> web.Response:
    """Find sites by ID

    Returns a report based on a site ID

    :param id: ID that needs to be fetched
    :type id: int
    :param _from: Start of the report, format YYYY-MM-DD, default today-30day 
    :type _from: str
    :param to: End of the report, format YYYY-MM-DD, default today
    :type to: str
    :param reports: Type of reports separate by comas: Ga,Logs,Uptime
    :type reports: str
    :param log_type: Type of the log to show in the report
    :type log_type: str
    :param compare: Define if you want show previous values in Google Analytics graph
    :type compare: int

    """
    return web.Response(status=200)

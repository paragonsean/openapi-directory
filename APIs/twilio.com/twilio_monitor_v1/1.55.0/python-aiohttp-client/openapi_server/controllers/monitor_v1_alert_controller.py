from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_alert_response import ListAlertResponse
from openapi_server.models.monitor_v1_alert_instance import MonitorV1AlertInstance
from openapi_server import util


async def fetch_alert(request: web.Request, sid) -> web.Response:
    """fetch_alert

    

    :param sid: The SID of the Alert resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_alert(request: web.Request, log_level=None, start_date=None, end_date=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_alert

    

    :param log_level: Only show alerts for this log-level.  Can be: &#x60;error&#x60;, &#x60;warning&#x60;, &#x60;notice&#x60;, or &#x60;debug&#x60;.
    :type log_level: str
    :param start_date: Only include alerts that occurred on or after this date and time. Specify the date and time in GMT and format as &#x60;YYYY-MM-DD&#x60; or &#x60;YYYY-MM-DDThh:mm:ssZ&#x60;. Queries for alerts older than 30 days are not supported.
    :type start_date: str
    :param end_date: Only include alerts that occurred on or before this date and time. Specify the date and time in GMT and format as &#x60;YYYY-MM-DD&#x60; or &#x60;YYYY-MM-DDThh:mm:ssZ&#x60;. Queries for alerts older than 30 days are not supported.
    :type end_date: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    start_date = util.deserialize_datetime(start_date)
    end_date = util.deserialize_datetime(end_date)
    return web.Response(status=200)

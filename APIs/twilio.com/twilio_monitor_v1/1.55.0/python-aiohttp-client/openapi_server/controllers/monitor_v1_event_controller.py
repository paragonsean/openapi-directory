from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_event_response import ListEventResponse
from openapi_server.models.monitor_v1_event import MonitorV1Event
from openapi_server import util


async def fetch_event(request: web.Request, sid) -> web.Response:
    """fetch_event

    

    :param sid: The SID of the Event resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_event(request: web.Request, actor_sid=None, event_type=None, resource_sid=None, source_ip_address=None, start_date=None, end_date=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_event

    Returns a list of events in the account, sorted by event-date.

    :param actor_sid: Only include events initiated by this Actor. Useful for auditing actions taken by specific users or API credentials.
    :type actor_sid: str
    :param event_type: Only include events of this [Event Type](https://www.twilio.com/docs/usage/monitor-events#event-types).
    :type event_type: str
    :param resource_sid: Only include events that refer to this resource. Useful for discovering the history of a specific resource.
    :type resource_sid: str
    :param source_ip_address: Only include events that originated from this IP address. Useful for tracking suspicious activity originating from the API or the Twilio Console.
    :type source_ip_address: str
    :param start_date: Only include events that occurred on or after this date. Specify the date in GMT and [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :type start_date: str
    :param end_date: Only include events that occurred on or before this date. Specify the date in GMT and [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
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

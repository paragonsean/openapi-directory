from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.event_log import EventLog
from openapi_server.models.event_log_collection import EventLogCollection
from openapi_server import util


async def get_event_log(request: web.Request, event_log_id) -> web.Response:
    """Get a log entry

    

    :param event_log_id: The event log ID.
    :type event_log_id: int

    """
    return web.Response(status=200)


async def get_event_logs(request: web.Request, limit=None, offset=None, order_by=None) -> web.Response:
    """List log entries

    List log entries from event log.

    :param limit: The numbers of items to return.
    :type limit: int
    :param offset: The number of items to skip before starting to collect the result set.
    :type offset: int
    :param order_by: The name of the field to order the results by. Prefix a field name with &#x60;-&#x60; to reverse the sort order.  *New in version 2.1.0* 
    :type order_by: str

    """
    return web.Response(status=200)

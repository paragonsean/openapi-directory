from typing import List, Dict
from aiohttp import web

from openapi_server.models.activity_log_entry_query_result import ActivityLogEntryQueryResult
from openapi_server import util


async def get_log_entries(request: web.Request, start_index=None, limit=None, min_date=None, has_user_id=None) -> web.Response:
    """Gets activity log entries.

    

    :param start_index: Optional. The record index to start at. All items with a lower index will be dropped from the results.
    :type start_index: int
    :param limit: Optional. The maximum number of records to return.
    :type limit: int
    :param min_date: Optional. The minimum date. Format &#x3D; ISO.
    :type min_date: str
    :param has_user_id: Optional. Filter log entries if it has user id, or not.
    :type has_user_id: bool

    """
    min_date = util.deserialize_datetime(min_date)
    return web.Response(status=200)

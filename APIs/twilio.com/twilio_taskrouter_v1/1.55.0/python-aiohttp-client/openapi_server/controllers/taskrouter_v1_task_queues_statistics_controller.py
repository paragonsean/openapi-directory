from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_task_queues_statistics_response import ListTaskQueuesStatisticsResponse
from openapi_server import util


async def list_task_queues_statistics(request: web.Request, workspace_sid, end_date=None, friendly_name=None, minutes=None, start_date=None, task_channel=None, split_by_wait_time=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_task_queues_statistics

    

    :param workspace_sid: The SID of the Workspace with the TaskQueues to read.
    :type workspace_sid: str
    :param end_date: Only calculate statistics from this date and time and earlier, specified in GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time.
    :type end_date: str
    :param friendly_name: The &#x60;friendly_name&#x60; of the TaskQueue statistics to read.
    :type friendly_name: str
    :param minutes: Only calculate statistics since this many minutes in the past. The default is 15 minutes.
    :type minutes: int
    :param start_date: Only calculate statistics from this date and time and later, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :type start_date: str
    :param task_channel: Only calculate statistics on this TaskChannel. Can be the TaskChannel&#39;s SID or its &#x60;unique_name&#x60;, such as &#x60;voice&#x60;, &#x60;sms&#x60;, or &#x60;default&#x60;.
    :type task_channel: str
    :param split_by_wait_time: A comma separated list of values that describes the thresholds, in seconds, to calculate statistics on. For each threshold specified, the number of Tasks canceled and reservations accepted above and below the specified thresholds in seconds are computed.
    :type split_by_wait_time: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    end_date = util.deserialize_datetime(end_date)
    start_date = util.deserialize_datetime(start_date)
    return web.Response(status=200)

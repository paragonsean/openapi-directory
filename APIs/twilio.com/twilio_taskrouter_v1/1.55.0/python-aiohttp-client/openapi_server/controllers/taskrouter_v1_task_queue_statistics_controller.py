from typing import List, Dict
from aiohttp import web

from openapi_server.models.taskrouter_v1_workspace_task_queue_task_queue_statistics import TaskrouterV1WorkspaceTaskQueueTaskQueueStatistics
from openapi_server import util


async def fetch_task_queue_statistics(request: web.Request, workspace_sid, task_queue_sid, end_date=None, minutes=None, start_date=None, task_channel=None, split_by_wait_time=None) -> web.Response:
    """fetch_task_queue_statistics

    

    :param workspace_sid: The SID of the Workspace with the TaskQueue to fetch.
    :type workspace_sid: str
    :param task_queue_sid: The SID of the TaskQueue for which to fetch statistics.
    :type task_queue_sid: str
    :param end_date: Only calculate statistics from this date and time and earlier, specified in GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time.
    :type end_date: str
    :param minutes: Only calculate statistics since this many minutes in the past. The default is 15 minutes.
    :type minutes: int
    :param start_date: Only calculate statistics from this date and time and later, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :type start_date: str
    :param task_channel: Only calculate real-time and cumulative statistics for the specified TaskChannel. Can be the TaskChannel&#39;s SID or its &#x60;unique_name&#x60;, such as &#x60;voice&#x60;, &#x60;sms&#x60;, or &#x60;default&#x60;.
    :type task_channel: str
    :param split_by_wait_time: A comma separated list of values that describes the thresholds, in seconds, to calculate statistics on. For each threshold specified, the number of Tasks canceled and reservations accepted above and below the specified thresholds in seconds are computed.
    :type split_by_wait_time: str

    """
    end_date = util.deserialize_datetime(end_date)
    start_date = util.deserialize_datetime(start_date)
    return web.Response(status=200)

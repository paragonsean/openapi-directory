from typing import List, Dict
from aiohttp import web

from openapi_server.models.taskrouter_v1_workspace_worker_worker_statistics import TaskrouterV1WorkspaceWorkerWorkerStatistics
from openapi_server import util


async def fetch_worker_statistics(request: web.Request, workspace_sid, minutes=None, start_date=None, end_date=None, task_queue_sid=None, task_queue_name=None, friendly_name=None, task_channel=None) -> web.Response:
    """fetch_worker_statistics

    

    :param workspace_sid: The SID of the Workspace with the Worker to fetch.
    :type workspace_sid: str
    :param minutes: Only calculate statistics since this many minutes in the past. The default 15 minutes. This is helpful for displaying statistics for the last 15 minutes, 240 minutes (4 hours), and 480 minutes (8 hours) to see trends.
    :type minutes: int
    :param start_date: Only calculate statistics from this date and time and later, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :type start_date: str
    :param end_date: Only calculate statistics from this date and time and earlier, specified in GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time.
    :type end_date: str
    :param task_queue_sid: The SID of the TaskQueue for which to fetch Worker statistics.
    :type task_queue_sid: str
    :param task_queue_name: The &#x60;friendly_name&#x60; of the TaskQueue for which to fetch Worker statistics.
    :type task_queue_name: str
    :param friendly_name: Only include Workers with &#x60;friendly_name&#x60; values that match this parameter.
    :type friendly_name: str
    :param task_channel: Only calculate statistics on this TaskChannel. Can be the TaskChannel&#39;s SID or its &#x60;unique_name&#x60;, such as &#x60;voice&#x60;, &#x60;sms&#x60;, or &#x60;default&#x60;.
    :type task_channel: str

    """
    start_date = util.deserialize_datetime(start_date)
    end_date = util.deserialize_datetime(end_date)
    return web.Response(status=200)

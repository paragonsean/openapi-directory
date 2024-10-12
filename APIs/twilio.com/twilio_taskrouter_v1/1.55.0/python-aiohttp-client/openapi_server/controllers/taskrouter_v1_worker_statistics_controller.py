from typing import List, Dict
from aiohttp import web

from openapi_server.models.taskrouter_v1_workspace_worker_worker_instance_statistics import TaskrouterV1WorkspaceWorkerWorkerInstanceStatistics
from openapi_server import util


async def fetch_worker_instance_statistics(request: web.Request, workspace_sid, worker_sid, minutes=None, start_date=None, end_date=None, task_channel=None) -> web.Response:
    """fetch_worker_instance_statistics

    

    :param workspace_sid: The SID of the Workspace with the WorkerChannel to fetch.
    :type workspace_sid: str
    :param worker_sid: The SID of the Worker with the WorkerChannel to fetch.
    :type worker_sid: str
    :param minutes: Only calculate statistics since this many minutes in the past. The default 15 minutes. This is helpful for displaying statistics for the last 15 minutes, 240 minutes (4 hours), and 480 minutes (8 hours) to see trends.
    :type minutes: int
    :param start_date: Only calculate statistics from this date and time and later, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :type start_date: str
    :param end_date: Only include usage that occurred on or before this date, specified in GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time.
    :type end_date: str
    :param task_channel: Only calculate statistics on this TaskChannel. Can be the TaskChannel&#39;s SID or its &#x60;unique_name&#x60;, such as &#x60;voice&#x60;, &#x60;sms&#x60;, or &#x60;default&#x60;.
    :type task_channel: str

    """
    start_date = util.deserialize_datetime(start_date)
    end_date = util.deserialize_datetime(end_date)
    return web.Response(status=200)

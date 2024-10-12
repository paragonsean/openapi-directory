from typing import List, Dict
from aiohttp import web

from openapi_server.models.taskrouter_v1_workspace_worker_workers_cumulative_statistics import TaskrouterV1WorkspaceWorkerWorkersCumulativeStatistics
from openapi_server import util


async def fetch_workers_cumulative_statistics(request: web.Request, workspace_sid, end_date=None, minutes=None, start_date=None, task_channel=None) -> web.Response:
    """fetch_workers_cumulative_statistics

    

    :param workspace_sid: The SID of the Workspace with the resource to fetch.
    :type workspace_sid: str
    :param end_date: Only calculate statistics from this date and time and earlier, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :type end_date: str
    :param minutes: Only calculate statistics since this many minutes in the past. The default 15 minutes. This is helpful for displaying statistics for the last 15 minutes, 240 minutes (4 hours), and 480 minutes (8 hours) to see trends.
    :type minutes: int
    :param start_date: Only calculate statistics from this date and time and later, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :type start_date: str
    :param task_channel: Only calculate cumulative statistics on this TaskChannel. Can be the TaskChannel&#39;s SID or its &#x60;unique_name&#x60;, such as &#x60;voice&#x60;, &#x60;sms&#x60;, or &#x60;default&#x60;.
    :type task_channel: str

    """
    end_date = util.deserialize_datetime(end_date)
    start_date = util.deserialize_datetime(start_date)
    return web.Response(status=200)

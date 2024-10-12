from typing import List, Dict
from aiohttp import web

from openapi_server.models.taskrouter_v1_workspace_workspace_cumulative_statistics import TaskrouterV1WorkspaceWorkspaceCumulativeStatistics
from openapi_server import util


async def fetch_workspace_cumulative_statistics(request: web.Request, workspace_sid, end_date=None, minutes=None, start_date=None, task_channel=None, split_by_wait_time=None) -> web.Response:
    """fetch_workspace_cumulative_statistics

    

    :param workspace_sid: The SID of the Workspace to fetch.
    :type workspace_sid: str
    :param end_date: Only include usage that occurred on or before this date, specified in GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time.
    :type end_date: str
    :param minutes: Only calculate statistics since this many minutes in the past. The default 15 minutes. This is helpful for displaying statistics for the last 15 minutes, 240 minutes (4 hours), and 480 minutes (8 hours) to see trends.
    :type minutes: int
    :param start_date: Only calculate statistics from this date and time and later, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :type start_date: str
    :param task_channel: Only calculate cumulative statistics on this TaskChannel. Can be the TaskChannel&#39;s SID or its &#x60;unique_name&#x60;, such as &#x60;voice&#x60;, &#x60;sms&#x60;, or &#x60;default&#x60;.
    :type task_channel: str
    :param split_by_wait_time: A comma separated list of values that describes the thresholds, in seconds, to calculate statistics on. For each threshold specified, the number of Tasks canceled and reservations accepted above and below the specified thresholds in seconds are computed. For example, &#x60;5,30&#x60; would show splits of Tasks that were canceled or accepted before and after 5 seconds and before and after 30 seconds. This can be used to show short abandoned Tasks or Tasks that failed to meet an SLA. TaskRouter will calculate statistics on up to 10,000 Tasks for any given threshold.
    :type split_by_wait_time: str

    """
    end_date = util.deserialize_datetime(end_date)
    start_date = util.deserialize_datetime(start_date)
    return web.Response(status=200)

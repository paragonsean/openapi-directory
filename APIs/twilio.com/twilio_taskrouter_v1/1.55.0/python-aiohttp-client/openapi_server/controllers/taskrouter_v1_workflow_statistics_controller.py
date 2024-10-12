from typing import List, Dict
from aiohttp import web

from openapi_server.models.taskrouter_v1_workspace_workflow_workflow_statistics import TaskrouterV1WorkspaceWorkflowWorkflowStatistics
from openapi_server import util


async def fetch_workflow_statistics(request: web.Request, workspace_sid, workflow_sid, minutes=None, start_date=None, end_date=None, task_channel=None, split_by_wait_time=None) -> web.Response:
    """fetch_workflow_statistics

    

    :param workspace_sid: The SID of the Workspace with the Workflow to fetch.
    :type workspace_sid: str
    :param workflow_sid: Returns the list of Tasks that are being controlled by the Workflow with the specified SID value.
    :type workflow_sid: str
    :param minutes: Only calculate statistics since this many minutes in the past. The default 15 minutes. This is helpful for displaying statistics for the last 15 minutes, 240 minutes (4 hours), and 480 minutes (8 hours) to see trends.
    :type minutes: int
    :param start_date: Only calculate statistics from this date and time and later, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :type start_date: str
    :param end_date: Only calculate statistics from this date and time and earlier, specified in GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time.
    :type end_date: str
    :param task_channel: Only calculate real-time statistics on this TaskChannel. Can be the TaskChannel&#39;s SID or its &#x60;unique_name&#x60;, such as &#x60;voice&#x60;, &#x60;sms&#x60;, or &#x60;default&#x60;.
    :type task_channel: str
    :param split_by_wait_time: A comma separated list of values that describes the thresholds, in seconds, to calculate statistics on. For each threshold specified, the number of Tasks canceled and reservations accepted above and below the specified thresholds in seconds are computed. For example, &#x60;5,30&#x60; would show splits of Tasks that were canceled or accepted before and after 5 seconds and before and after 30 seconds. This can be used to show short abandoned Tasks or Tasks that failed to meet an SLA.
    :type split_by_wait_time: str

    """
    start_date = util.deserialize_datetime(start_date)
    end_date = util.deserialize_datetime(end_date)
    return web.Response(status=200)

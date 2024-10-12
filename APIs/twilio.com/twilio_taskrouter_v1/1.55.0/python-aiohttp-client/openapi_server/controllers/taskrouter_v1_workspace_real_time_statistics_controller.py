from typing import List, Dict
from aiohttp import web

from openapi_server.models.taskrouter_v1_workspace_workspace_real_time_statistics import TaskrouterV1WorkspaceWorkspaceRealTimeStatistics
from openapi_server import util


async def fetch_workspace_real_time_statistics(request: web.Request, workspace_sid, task_channel=None) -> web.Response:
    """fetch_workspace_real_time_statistics

    

    :param workspace_sid: The SID of the Workspace to fetch.
    :type workspace_sid: str
    :param task_channel: Only calculate real-time statistics on this TaskChannel. Can be the TaskChannel&#39;s SID or its &#x60;unique_name&#x60;, such as &#x60;voice&#x60;, &#x60;sms&#x60;, or &#x60;default&#x60;.
    :type task_channel: str

    """
    return web.Response(status=200)

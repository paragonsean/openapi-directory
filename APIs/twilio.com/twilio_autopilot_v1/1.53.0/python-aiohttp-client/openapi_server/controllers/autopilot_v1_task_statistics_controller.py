from typing import List, Dict
from aiohttp import web

from openapi_server.models.autopilot_v1_assistant_task_task_statistics import AutopilotV1AssistantTaskTaskStatistics
from openapi_server import util


async def fetch_task_statistics(request: web.Request, assistant_sid, task_sid) -> web.Response:
    """fetch_task_statistics

    

    :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resource to fetch.
    :type assistant_sid: str
    :param task_sid: The SID of the [Task](https://www.twilio.com/docs/autopilot/api/task) that is associated with the resource to fetch.
    :type task_sid: str

    """
    return web.Response(status=200)

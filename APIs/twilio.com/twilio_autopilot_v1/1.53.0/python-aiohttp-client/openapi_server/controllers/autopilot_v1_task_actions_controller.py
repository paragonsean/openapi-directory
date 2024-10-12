from typing import List, Dict
from aiohttp import web

from openapi_server.models.autopilot_v1_assistant_task_task_actions import AutopilotV1AssistantTaskTaskActions
from openapi_server import util


async def fetch_task_actions(request: web.Request, assistant_sid, task_sid) -> web.Response:
    """fetch_task_actions

    Returns JSON actions for the Task.

    :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the Task for which the task actions to fetch were defined.
    :type assistant_sid: str
    :param task_sid: The SID of the [Task](https://www.twilio.com/docs/autopilot/api/task) for which the task actions to fetch were defined.
    :type task_sid: str

    """
    return web.Response(status=200)


async def update_task_actions(request: web.Request, assistant_sid, task_sid, actions=None) -> web.Response:
    """update_task_actions

    Updates the actions of an Task identified by {TaskSid} or {TaskUniqueName}.

    :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the Task for which the task actions to update were defined.
    :type assistant_sid: str
    :param task_sid: The SID of the [Task](https://www.twilio.com/docs/autopilot/api/task) for which the task actions to update were defined.
    :type task_sid: str
    :param actions: The JSON string that specifies the [actions](https://www.twilio.com/docs/autopilot/actions) that instruct the Assistant on how to perform the task.
    :type actions: dict | bytes

    """
    actions = object.from_dict(actions)
    return web.Response(status=200)

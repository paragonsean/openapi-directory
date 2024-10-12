from typing import List, Dict
from aiohttp import web

from openapi_server.models.activity import Activity
from openapi_server import util


async def v2_activities_json_post(request: web.Request, action_id=None, task_id=None) -> web.Response:
    """Create an activity

    Creates an activity. An activity will mark the associated action as completed. Currently, only certain action types can have an activity explicitly created for them. 

    :param action_id: Action that is being completed. This will validate that the action is still valid before completed it. The same action can never be successfully passed twice to this endpoint. The action must have a type of &#39;integration&#39;. 
    :type action_id: int
    :param task_id: Task that is being completed. This will validate that the task is still valid before completed it. The same action can never be successfully passed twice to this endpoint. The task must have a type of &#39;integration&#39;. 
    :type task_id: int

    """
    return web.Response(status=200)

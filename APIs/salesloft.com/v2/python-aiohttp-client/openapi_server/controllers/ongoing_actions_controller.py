from typing import List, Dict
from aiohttp import web

from openapi_server.models.action import Action
from openapi_server import util


async def v2_ongoing_actions_json_post(request: web.Request, action_id=None) -> web.Response:
    """Create an ongoing action

    Creates an ongoing action. An ongoing action is an action that is not yet completed, but progress has been made towards the completion. The user should not need to do anything for an ongoing action to be completed. An ongoing action can be later completed by creating an activity.  Ongoing actions are marked as status&#x3D;pending_activity. 

    :param action_id: Action that is being marked ongoing. This will validate that the action is still valid before modifying it. Ongoing actions can not be marked ongoing. 
    :type action_id: int

    """
    return web.Response(status=200)

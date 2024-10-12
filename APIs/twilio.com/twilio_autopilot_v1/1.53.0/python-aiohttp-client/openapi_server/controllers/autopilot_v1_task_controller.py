from typing import List, Dict
from aiohttp import web

from openapi_server.models.autopilot_v1_assistant_task import AutopilotV1AssistantTask
from openapi_server.models.list_task_response import ListTaskResponse
from openapi_server import util


async def create_task(request: web.Request, assistant_sid, unique_name, actions=None, actions_url=None, friendly_name=None) -> web.Response:
    """create_task

    

    :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the new resource.
    :type assistant_sid: str
    :param unique_name: An application-defined string that uniquely identifies the new resource. It can be used as an alternative to the &#x60;sid&#x60; in the URL path to address the resource. This value must be unique and 64 characters or less in length.
    :type unique_name: str
    :param actions: The JSON string that specifies the [actions](https://www.twilio.com/docs/autopilot/actions) that instruct the Assistant on how to perform the task. It is optional and not unique.
    :type actions: dict | bytes
    :param actions_url: The URL from which the Assistant can fetch actions.
    :type actions_url: str
    :param friendly_name: A descriptive string that you create to describe the new resource. It is not unique and can be up to 255 characters long.
    :type friendly_name: str

    """
    actions = object.from_dict(actions)
    return web.Response(status=200)


async def delete_task(request: web.Request, assistant_sid, sid) -> web.Response:
    """delete_task

    

    :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resources to delete.
    :type assistant_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Task resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_task(request: web.Request, assistant_sid, sid) -> web.Response:
    """fetch_task

    

    :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resource to fetch.
    :type assistant_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Task resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_task(request: web.Request, assistant_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_task

    

    :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resources to read.
    :type assistant_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_task(request: web.Request, assistant_sid, sid, actions=None, actions_url=None, friendly_name=None, unique_name=None) -> web.Response:
    """update_task

    

    :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resource to update.
    :type assistant_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Task resource to update.
    :type sid: str
    :param actions: The JSON string that specifies the [actions](https://www.twilio.com/docs/autopilot/actions) that instruct the Assistant on how to perform the task.
    :type actions: dict | bytes
    :param actions_url: The URL from which the Assistant can fetch actions.
    :type actions_url: str
    :param friendly_name: A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
    :type friendly_name: str
    :param unique_name: An application-defined string that uniquely identifies the resource. This value must be 64 characters or less in length and be unique. It can be used as an alternative to the &#x60;sid&#x60; in the URL path to address the resource.
    :type unique_name: str

    """
    actions = object.from_dict(actions)
    return web.Response(status=200)

from typing import List, Dict
from aiohttp import web

from openapi_server.models.autopilot_v1_assistant_task_field import AutopilotV1AssistantTaskField
from openapi_server.models.list_field_response import ListFieldResponse
from openapi_server import util


async def create_field(request: web.Request, assistant_sid, task_sid, field_type, unique_name) -> web.Response:
    """create_field

    

    :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the Task associated with the new resource.
    :type assistant_sid: str
    :param task_sid: The SID of the [Task](https://www.twilio.com/docs/autopilot/api/task) resource associated with the new Field resource.
    :type task_sid: str
    :param field_type: The Field Type of the new field. Can be: a [Built-in Field Type](https://www.twilio.com/docs/autopilot/built-in-field-types), the &#x60;unique_name&#x60;, or the &#x60;sid&#x60; of a custom Field Type.
    :type field_type: str
    :param unique_name: An application-defined string that uniquely identifies the new resource. This value must be a unique string of no more than 64 characters. It can be used as an alternative to the &#x60;sid&#x60; in the URL path to address the resource.
    :type unique_name: str

    """
    return web.Response(status=200)


async def delete_field(request: web.Request, assistant_sid, task_sid, sid) -> web.Response:
    """delete_field

    

    :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the Task associated with the resources to delete.
    :type assistant_sid: str
    :param task_sid: The SID of the [Task](https://www.twilio.com/docs/autopilot/api/task) resource associated with the Field resource to delete.
    :type task_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Field resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_field(request: web.Request, assistant_sid, task_sid, sid) -> web.Response:
    """fetch_field

    

    :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the Task associated with the resource to fetch.
    :type assistant_sid: str
    :param task_sid: The SID of the [Task](https://www.twilio.com/docs/autopilot/api/task) resource associated with the Field resource to fetch.
    :type task_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Field resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_field(request: web.Request, assistant_sid, task_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_field

    

    :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the Task associated with the resources to read.
    :type assistant_sid: str
    :param task_sid: The SID of the [Task](https://www.twilio.com/docs/autopilot/api/task) resource associated with the Field resources to read.
    :type task_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)

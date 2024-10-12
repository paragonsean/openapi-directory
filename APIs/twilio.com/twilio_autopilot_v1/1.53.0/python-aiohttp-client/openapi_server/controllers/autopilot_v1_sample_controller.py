from typing import List, Dict
from aiohttp import web

from openapi_server.models.autopilot_v1_assistant_task_sample import AutopilotV1AssistantTaskSample
from openapi_server.models.list_sample_response import ListSampleResponse
from openapi_server import util


async def create_sample(request: web.Request, assistant_sid, task_sid, language, tagged_text, source_channel=None) -> web.Response:
    """create_sample

    

    :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the Task associated with the new resource.
    :type assistant_sid: str
    :param task_sid: The SID of the [Task](https://www.twilio.com/docs/autopilot/api/task) associated with the Sample resource to create.
    :type task_sid: str
    :param language: The [ISO language-country](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html) string that specifies the language used for the new sample. For example: &#x60;en-US&#x60;.
    :type language: str
    :param tagged_text: The text example of how end users might express the task. The sample can contain [Field tag blocks](https://www.twilio.com/docs/autopilot/api/task-sample#field-tagging).
    :type tagged_text: str
    :param source_channel: The communication channel from which the new sample was captured. Can be: &#x60;voice&#x60;, &#x60;sms&#x60;, &#x60;chat&#x60;, &#x60;alexa&#x60;, &#x60;google-assistant&#x60;, &#x60;slack&#x60;, or null if not included.
    :type source_channel: str

    """
    return web.Response(status=200)


async def delete_sample(request: web.Request, assistant_sid, task_sid, sid) -> web.Response:
    """delete_sample

    

    :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the Task associated with the resources to delete.
    :type assistant_sid: str
    :param task_sid: The SID of the [Task](https://www.twilio.com/docs/autopilot/api/task) associated with the Sample resource to delete.
    :type task_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Sample resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_sample(request: web.Request, assistant_sid, task_sid, sid) -> web.Response:
    """fetch_sample

    

    :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the Task associated with the resource to fetch.
    :type assistant_sid: str
    :param task_sid: The SID of the [Task](https://www.twilio.com/docs/autopilot/api/task) associated with the Sample resource to create.
    :type task_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Sample resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_sample(request: web.Request, assistant_sid, task_sid, language=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_sample

    

    :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the Task associated with the resources to read.
    :type assistant_sid: str
    :param task_sid: The SID of the [Task](https://www.twilio.com/docs/autopilot/api/task) associated with the Sample resources to read.
    :type task_sid: str
    :param language: The [ISO language-country](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html) string that specifies the language used for the sample. For example: &#x60;en-US&#x60;.
    :type language: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_sample(request: web.Request, assistant_sid, task_sid, sid, language=None, source_channel=None, tagged_text=None) -> web.Response:
    """update_sample

    

    :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the Task associated with the resource to update.
    :type assistant_sid: str
    :param task_sid: The SID of the [Task](https://www.twilio.com/docs/autopilot/api/task) associated with the Sample resource to update.
    :type task_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Sample resource to update.
    :type sid: str
    :param language: The [ISO language-country](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html) string that specifies the language used for the sample. For example: &#x60;en-US&#x60;.
    :type language: str
    :param source_channel: The communication channel from which the sample was captured. Can be: &#x60;voice&#x60;, &#x60;sms&#x60;, &#x60;chat&#x60;, &#x60;alexa&#x60;, &#x60;google-assistant&#x60;, &#x60;slack&#x60;, or null if not included.
    :type source_channel: str
    :param tagged_text: The text example of how end users might express the task. The sample can contain [Field tag blocks](https://www.twilio.com/docs/autopilot/api/task-sample#field-tagging).
    :type tagged_text: str

    """
    return web.Response(status=200)

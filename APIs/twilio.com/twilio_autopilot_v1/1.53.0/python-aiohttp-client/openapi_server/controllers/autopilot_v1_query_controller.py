from typing import List, Dict
from aiohttp import web

from openapi_server.models.autopilot_v1_assistant_query import AutopilotV1AssistantQuery
from openapi_server.models.list_query_response import ListQueryResponse
from openapi_server import util


async def create_query(request: web.Request, assistant_sid, language, query, model_build=None, tasks=None) -> web.Response:
    """create_query

    

    :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the new resource.
    :type assistant_sid: str
    :param language: The [ISO language-country](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html) string that specifies the language used for the new query. For example: &#x60;en-US&#x60;.
    :type language: str
    :param query: The end-user&#39;s natural language input. It can be up to 2048 characters long.
    :type query: str
    :param model_build: The SID or unique name of the [Model Build](https://www.twilio.com/docs/autopilot/api/model-build) to be queried.
    :type model_build: str
    :param tasks: The list of tasks to limit the new query to. Tasks are expressed as a comma-separated list of task &#x60;unique_name&#x60; values. For example, &#x60;task-unique_name-1, task-unique_name-2&#x60;. Listing specific tasks is useful to constrain the paths that a user can take.
    :type tasks: str

    """
    return web.Response(status=200)


async def delete_query(request: web.Request, assistant_sid, sid) -> web.Response:
    """delete_query

    

    :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resources to delete.
    :type assistant_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Query resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_query(request: web.Request, assistant_sid, sid) -> web.Response:
    """fetch_query

    

    :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resource to fetch.
    :type assistant_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Query resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_query(request: web.Request, assistant_sid, language=None, model_build=None, status=None, dialogue_sid=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_query

    

    :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resources to read.
    :type assistant_sid: str
    :param language: The [ISO language-country](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html) string that specifies the language used by the Query resources to read. For example: &#x60;en-US&#x60;.
    :type language: str
    :param model_build: The SID or unique name of the [Model Build](https://www.twilio.com/docs/autopilot/api/model-build) to be queried.
    :type model_build: str
    :param status: The status of the resources to read. Can be: &#x60;pending-review&#x60;, &#x60;reviewed&#x60;, or &#x60;discarded&#x60;
    :type status: str
    :param dialogue_sid: The SID of the [Dialogue](https://www.twilio.com/docs/autopilot/api/dialogue).
    :type dialogue_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_query(request: web.Request, assistant_sid, sid, sample_sid=None, status=None) -> web.Response:
    """update_query

    

    :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resource to update.
    :type assistant_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Query resource to update.
    :type sid: str
    :param sample_sid: The SID of an optional reference to the [Sample](https://www.twilio.com/docs/autopilot/api/task-sample) created from the query.
    :type sample_sid: str
    :param status: The new status of the resource. Can be: &#x60;pending-review&#x60;, &#x60;reviewed&#x60;, or &#x60;discarded&#x60;
    :type status: str

    """
    return web.Response(status=200)

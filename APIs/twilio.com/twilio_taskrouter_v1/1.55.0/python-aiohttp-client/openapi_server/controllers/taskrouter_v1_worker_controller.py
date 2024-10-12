from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_worker_response import ListWorkerResponse
from openapi_server.models.taskrouter_v1_workspace_worker import TaskrouterV1WorkspaceWorker
from openapi_server import util


async def create_worker(request: web.Request, workspace_sid, friendly_name, activity_sid=None, attributes=None) -> web.Response:
    """create_worker

    

    :param workspace_sid: The SID of the Workspace that the new Worker belongs to.
    :type workspace_sid: str
    :param friendly_name: A descriptive string that you create to describe the new Worker. It can be up to 64 characters long.
    :type friendly_name: str
    :param activity_sid: The SID of a valid Activity that will describe the new Worker&#39;s initial state. See [Activities](https://www.twilio.com/docs/taskrouter/api/activity) for more information. If not provided, the new Worker&#39;s initial state is the &#x60;default_activity_sid&#x60; configured on the Workspace.
    :type activity_sid: str
    :param attributes: A valid JSON string that describes the new Worker. For example: &#x60;{ \\\&quot;email\\\&quot;: \\\&quot;Bob@example.com\\\&quot;, \\\&quot;phone\\\&quot;: \\\&quot;+5095551234\\\&quot; }&#x60;. This data is passed to the &#x60;assignment_callback_url&#x60; when TaskRouter assigns a Task to the Worker. Defaults to {}.
    :type attributes: str

    """
    return web.Response(status=200)


async def delete_worker(request: web.Request, workspace_sid, sid, if_match=None) -> web.Response:
    """delete_worker

    

    :param workspace_sid: The SID of the Workspace with the Worker to delete.
    :type workspace_sid: str
    :param sid: The SID of the Worker resource to delete.
    :type sid: str
    :param if_match: The If-Match HTTP request header
    :type if_match: str

    """
    return web.Response(status=200)


async def fetch_worker(request: web.Request, workspace_sid, sid) -> web.Response:
    """fetch_worker

    

    :param workspace_sid: The SID of the Workspace with the Worker to fetch.
    :type workspace_sid: str
    :param sid: The SID of the Worker resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_worker(request: web.Request, workspace_sid, activity_name=None, activity_sid=None, available=None, friendly_name=None, target_workers_expression=None, task_queue_name=None, task_queue_sid=None, ordering=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_worker

    

    :param workspace_sid: The SID of the Workspace with the Workers to read.
    :type workspace_sid: str
    :param activity_name: The &#x60;activity_name&#x60; of the Worker resources to read.
    :type activity_name: str
    :param activity_sid: The &#x60;activity_sid&#x60; of the Worker resources to read.
    :type activity_sid: str
    :param available: Whether to return only Worker resources that are available or unavailable. Can be &#x60;true&#x60;, &#x60;1&#x60;, or &#x60;yes&#x60; to return Worker resources that are available, and &#x60;false&#x60;, or any value returns the Worker resources that are not available.
    :type available: str
    :param friendly_name: The &#x60;friendly_name&#x60; of the Worker resources to read.
    :type friendly_name: str
    :param target_workers_expression: Filter by Workers that would match an expression. In addition to fields in the workers&#39; attributes, the expression can include the following worker fields: &#x60;sid&#x60;, &#x60;friendly_name&#x60;, &#x60;activity_sid&#x60;, or &#x60;activity_name&#x60;
    :type target_workers_expression: str
    :param task_queue_name: The &#x60;friendly_name&#x60; of the TaskQueue that the Workers to read are eligible for.
    :type task_queue_name: str
    :param task_queue_sid: The SID of the TaskQueue that the Workers to read are eligible for.
    :type task_queue_sid: str
    :param ordering: Sorting parameter for Workers
    :type ordering: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_worker(request: web.Request, workspace_sid, sid, if_match=None, activity_sid=None, attributes=None, friendly_name=None, reject_pending_reservations=None) -> web.Response:
    """update_worker

    

    :param workspace_sid: The SID of the Workspace with the Worker to update.
    :type workspace_sid: str
    :param sid: The SID of the Worker resource to update.
    :type sid: str
    :param if_match: The If-Match HTTP request header
    :type if_match: str
    :param activity_sid: The SID of a valid Activity that will describe the Worker&#39;s initial state. See [Activities](https://www.twilio.com/docs/taskrouter/api/activity) for more information.
    :type activity_sid: str
    :param attributes: The JSON string that describes the Worker. For example: &#x60;{ \\\&quot;email\\\&quot;: \\\&quot;Bob@example.com\\\&quot;, \\\&quot;phone\\\&quot;: \\\&quot;+5095551234\\\&quot; }&#x60;. This data is passed to the &#x60;assignment_callback_url&#x60; when TaskRouter assigns a Task to the Worker. Defaults to {}.
    :type attributes: str
    :param friendly_name: A descriptive string that you create to describe the Worker. It can be up to 64 characters long.
    :type friendly_name: str
    :param reject_pending_reservations: Whether to reject the Worker&#39;s pending reservations. This option is only valid if the Worker&#39;s new [Activity](https://www.twilio.com/docs/taskrouter/api/activity) resource has its &#x60;availability&#x60; property set to &#x60;False&#x60;.
    :type reject_pending_reservations: bool

    """
    return web.Response(status=200)

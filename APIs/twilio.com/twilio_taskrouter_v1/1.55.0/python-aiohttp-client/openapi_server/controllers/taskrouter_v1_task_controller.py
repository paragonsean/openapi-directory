from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_task_response import ListTaskResponse
from openapi_server.models.task_enum_status import TaskEnumStatus
from openapi_server.models.taskrouter_v1_workspace_task import TaskrouterV1WorkspaceTask
from openapi_server import util


async def create_task(request: web.Request, workspace_sid, attributes=None, priority=None, task_channel=None, timeout=None, virtual_start_time=None, workflow_sid=None) -> web.Response:
    """create_task

    

    :param workspace_sid: The SID of the Workspace that the new Task belongs to.
    :type workspace_sid: str
    :param attributes: A URL-encoded JSON string with the attributes of the new task. This value is passed to the Workflow&#39;s &#x60;assignment_callback_url&#x60; when the Task is assigned to a Worker. For example: &#x60;{ \\\&quot;task_type\\\&quot;: \\\&quot;call\\\&quot;, \\\&quot;twilio_call_sid\\\&quot;: \\\&quot;CAxxx\\\&quot;, \\\&quot;customer_ticket_number\\\&quot;: \\\&quot;12345\\\&quot; }&#x60;.
    :type attributes: str
    :param priority: The priority to assign the new task and override the default. When supplied, the new Task will have this priority unless it matches a Workflow Target with a Priority set. When not supplied, the new Task will have the priority of the matching Workflow Target. Value can be 0 to 2^31^ (2,147,483,647).
    :type priority: int
    :param task_channel: When MultiTasking is enabled, specify the TaskChannel by passing either its &#x60;unique_name&#x60; or &#x60;sid&#x60;. Default value is &#x60;default&#x60;.
    :type task_channel: str
    :param timeout: The amount of time in seconds the new task can live before being assigned. Can be up to a maximum of 2 weeks (1,209,600 seconds). The default value is 24 hours (86,400 seconds). On timeout, the &#x60;task.canceled&#x60; event will fire with description &#x60;Task TTL Exceeded&#x60;.
    :type timeout: int
    :param virtual_start_time: The virtual start time to assign the new task and override the default. When supplied, the new task will have this virtual start time. When not supplied, the new task will have the virtual start time equal to &#x60;date_created&#x60;. Value can&#39;t be in the future.
    :type virtual_start_time: str
    :param workflow_sid: The SID of the Workflow that you would like to handle routing for the new Task. If there is only one Workflow defined for the Workspace that you are posting the new task to, this parameter is optional.
    :type workflow_sid: str

    """
    virtual_start_time = util.deserialize_datetime(virtual_start_time)
    return web.Response(status=200)


async def delete_task(request: web.Request, workspace_sid, sid, if_match=None) -> web.Response:
    """delete_task

    

    :param workspace_sid: The SID of the Workspace with the Task to delete.
    :type workspace_sid: str
    :param sid: The SID of the Task resource to delete.
    :type sid: str
    :param if_match: If provided, deletes this Task if (and only if) the [ETag](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag) header of the Task matches the provided value. This matches the semantics of (and is implemented with) the HTTP [If-Match header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match).
    :type if_match: str

    """
    return web.Response(status=200)


async def fetch_task(request: web.Request, workspace_sid, sid) -> web.Response:
    """fetch_task

    

    :param workspace_sid: The SID of the Workspace with the Task to fetch.
    :type workspace_sid: str
    :param sid: The SID of the Task resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_task(request: web.Request, workspace_sid, priority=None, assignment_status=None, workflow_sid=None, workflow_name=None, task_queue_sid=None, task_queue_name=None, evaluate_task_attributes=None, ordering=None, has_addons=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_task

    

    :param workspace_sid: The SID of the Workspace with the Tasks to read.
    :type workspace_sid: str
    :param priority: The priority value of the Tasks to read. Returns the list of all Tasks in the Workspace with the specified priority.
    :type priority: int
    :param assignment_status: The &#x60;assignment_status&#x60; of the Tasks you want to read. Can be: &#x60;pending&#x60;, &#x60;reserved&#x60;, &#x60;assigned&#x60;, &#x60;canceled&#x60;, &#x60;wrapping&#x60;, or &#x60;completed&#x60;. Returns all Tasks in the Workspace with the specified &#x60;assignment_status&#x60;.
    :type assignment_status: List[str]
    :param workflow_sid: The SID of the Workflow with the Tasks to read. Returns the Tasks controlled by the Workflow identified by this SID.
    :type workflow_sid: str
    :param workflow_name: The friendly name of the Workflow with the Tasks to read. Returns the Tasks controlled by the Workflow identified by this friendly name.
    :type workflow_name: str
    :param task_queue_sid: The SID of the TaskQueue with the Tasks to read. Returns the Tasks waiting in the TaskQueue identified by this SID.
    :type task_queue_sid: str
    :param task_queue_name: The &#x60;friendly_name&#x60; of the TaskQueue with the Tasks to read. Returns the Tasks waiting in the TaskQueue identified by this friendly name.
    :type task_queue_name: str
    :param evaluate_task_attributes: The attributes of the Tasks to read. Returns the Tasks that match the attributes specified in this parameter.
    :type evaluate_task_attributes: str
    :param ordering: How to order the returned Task resources. By default, Tasks are sorted by ascending DateCreated. This value is specified as: &#x60;Attribute:Order&#x60;, where &#x60;Attribute&#x60; can be either &#x60;DateCreated&#x60;, &#x60;Priority&#x60;, or &#x60;VirtualStartTime&#x60; and &#x60;Order&#x60; can be either &#x60;asc&#x60; or &#x60;desc&#x60;. For example, &#x60;Priority:desc&#x60; returns Tasks ordered in descending order of their Priority. Pairings of sort orders can be specified in a comma-separated list such as &#x60;Priority:desc,DateCreated:asc&#x60;, which returns the Tasks in descending Priority order and ascending DateCreated Order. The only ordering pairing not allowed is DateCreated and VirtualStartTime.
    :type ordering: str
    :param has_addons: Whether to read Tasks with Add-ons. If &#x60;true&#x60;, returns only Tasks with Add-ons. If &#x60;false&#x60;, returns only Tasks without Add-ons.
    :type has_addons: bool
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_task(request: web.Request, workspace_sid, sid, if_match=None, assignment_status=None, attributes=None, priority=None, reason=None, task_channel=None, virtual_start_time=None) -> web.Response:
    """update_task

    

    :param workspace_sid: The SID of the Workspace with the Task to update.
    :type workspace_sid: str
    :param sid: The SID of the Task resource to update.
    :type sid: str
    :param if_match: If provided, applies this mutation if (and only if) the [ETag](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag) header of the Task matches the provided value. This matches the semantics of (and is implemented with) the HTTP [If-Match header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match).
    :type if_match: str
    :param assignment_status: 
    :type assignment_status: str
    :param attributes: The JSON string that describes the custom attributes of the task.
    :type attributes: str
    :param priority: The Task&#39;s new priority value. When supplied, the Task takes on the specified priority unless it matches a Workflow Target with a Priority set. Value can be 0 to 2^31^ (2,147,483,647).
    :type priority: int
    :param reason: The reason that the Task was canceled or completed. This parameter is required only if the Task is canceled or completed. Setting this value queues the task for deletion and logs the reason.
    :type reason: str
    :param task_channel: When MultiTasking is enabled, specify the TaskChannel with the task to update. Can be the TaskChannel&#39;s SID or its &#x60;unique_name&#x60;, such as &#x60;voice&#x60;, &#x60;sms&#x60;, or &#x60;default&#x60;.
    :type task_channel: str
    :param virtual_start_time: The task&#39;s new virtual start time value. When supplied, the Task takes on the specified virtual start time. Value can&#39;t be in the future.
    :type virtual_start_time: str

    """
    virtual_start_time = util.deserialize_datetime(virtual_start_time)
    return web.Response(status=200)

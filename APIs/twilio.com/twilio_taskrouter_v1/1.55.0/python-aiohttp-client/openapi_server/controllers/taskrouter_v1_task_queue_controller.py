from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_task_queue_response import ListTaskQueueResponse
from openapi_server.models.task_queue_enum_task_order import TaskQueueEnumTaskOrder
from openapi_server.models.taskrouter_v1_workspace_task_queue import TaskrouterV1WorkspaceTaskQueue
from openapi_server import util


async def create_task_queue(request: web.Request, workspace_sid, friendly_name, assignment_activity_sid=None, max_reserved_workers=None, reservation_activity_sid=None, target_workers=None, task_order=None) -> web.Response:
    """create_task_queue

    

    :param workspace_sid: The SID of the Workspace that the new TaskQueue belongs to.
    :type workspace_sid: str
    :param friendly_name: A descriptive string that you create to describe the TaskQueue. For example &#x60;Support-Tier 1&#x60;, &#x60;Sales&#x60;, or &#x60;Escalation&#x60;.
    :type friendly_name: str
    :param assignment_activity_sid: The SID of the Activity to assign Workers when a task is assigned to them.
    :type assignment_activity_sid: str
    :param max_reserved_workers: The maximum number of Workers to reserve for the assignment of a Task in the queue. Can be an integer between 1 and 50, inclusive and defaults to 1.
    :type max_reserved_workers: int
    :param reservation_activity_sid: The SID of the Activity to assign Workers when a task is reserved for them.
    :type reservation_activity_sid: str
    :param target_workers: A string that describes the Worker selection criteria for any Tasks that enter the TaskQueue. For example, &#x60;&#39;\\\&quot;language\\\&quot; &#x3D;&#x3D; \\\&quot;spanish\\\&quot;&#39;&#x60;. The default value is &#x60;1&#x3D;&#x3D;1&#x60;. If this value is empty, Tasks will wait in the TaskQueue until they are deleted or moved to another TaskQueue. For more information about Worker selection, see [Describing Worker selection criteria](https://www.twilio.com/docs/taskrouter/api/taskqueues#target-workers).
    :type target_workers: str
    :param task_order: 
    :type task_order: str

    """
    return web.Response(status=200)


async def delete_task_queue(request: web.Request, workspace_sid, sid) -> web.Response:
    """delete_task_queue

    

    :param workspace_sid: The SID of the Workspace with the TaskQueue to delete.
    :type workspace_sid: str
    :param sid: The SID of the TaskQueue resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_task_queue(request: web.Request, workspace_sid, sid) -> web.Response:
    """fetch_task_queue

    

    :param workspace_sid: The SID of the Workspace with the TaskQueue to fetch.
    :type workspace_sid: str
    :param sid: The SID of the TaskQueue resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_task_queue(request: web.Request, workspace_sid, friendly_name=None, evaluate_worker_attributes=None, worker_sid=None, ordering=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_task_queue

    

    :param workspace_sid: The SID of the Workspace with the TaskQueue to read.
    :type workspace_sid: str
    :param friendly_name: The &#x60;friendly_name&#x60; of the TaskQueue resources to read.
    :type friendly_name: str
    :param evaluate_worker_attributes: The attributes of the Workers to read. Returns the TaskQueues with Workers that match the attributes specified in this parameter.
    :type evaluate_worker_attributes: str
    :param worker_sid: The SID of the Worker with the TaskQueue resources to read.
    :type worker_sid: str
    :param ordering: Sorting parameter for TaskQueues
    :type ordering: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_task_queue(request: web.Request, workspace_sid, sid, assignment_activity_sid=None, friendly_name=None, max_reserved_workers=None, reservation_activity_sid=None, target_workers=None, task_order=None) -> web.Response:
    """update_task_queue

    

    :param workspace_sid: The SID of the Workspace with the TaskQueue to update.
    :type workspace_sid: str
    :param sid: The SID of the TaskQueue resource to update.
    :type sid: str
    :param assignment_activity_sid: The SID of the Activity to assign Workers when a task is assigned for them.
    :type assignment_activity_sid: str
    :param friendly_name: A descriptive string that you create to describe the TaskQueue. For example &#x60;Support-Tier 1&#x60;, &#x60;Sales&#x60;, or &#x60;Escalation&#x60;.
    :type friendly_name: str
    :param max_reserved_workers: The maximum number of Workers to create reservations for the assignment of a task while in the queue. Maximum of 50.
    :type max_reserved_workers: int
    :param reservation_activity_sid: The SID of the Activity to assign Workers when a task is reserved for them.
    :type reservation_activity_sid: str
    :param target_workers: A string describing the Worker selection criteria for any Tasks that enter the TaskQueue. For example &#39;\\\&quot;language\\\&quot; &#x3D;&#x3D; \\\&quot;spanish\\\&quot;&#39; If no TargetWorkers parameter is provided, Tasks will wait in the queue until they are either deleted or moved to another queue. Additional examples on how to describing Worker selection criteria below.
    :type target_workers: str
    :param task_order: 
    :type task_order: str

    """
    return web.Response(status=200)

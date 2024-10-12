from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_resource_member_request_body import AddResourceMemberRequestBody
from openapi_server.models.error import Error
from openapi_server.models.label_mapping import LabelMapping
from openapi_server.models.label_response import LabelResponse
from openapi_server.models.labels_response import LabelsResponse
from openapi_server.models.logs import Logs
from openapi_server.models.resource_member import ResourceMember
from openapi_server.models.resource_members import ResourceMembers
from openapi_server.models.resource_owner import ResourceOwner
from openapi_server.models.resource_owners import ResourceOwners
from openapi_server.models.run import Run
from openapi_server.models.run_manually import RunManually
from openapi_server.models.runs import Runs
from openapi_server.models.task import Task
from openapi_server.models.task_create_request import TaskCreateRequest
from openapi_server.models.task_update_request import TaskUpdateRequest
from openapi_server.models.tasks import Tasks
from openapi_server import util


async def delete_tasks_id(request: web.Request, task_id, zap_trace_span=None) -> web.Response:
    """Delete a task

    Deletes a task and all associated records

    :param task_id: The ID of the task to delete.
    :type task_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def delete_tasks_id_labels_id(request: web.Request, task_id, label_id, zap_trace_span=None) -> web.Response:
    """Delete a label from a task

    

    :param task_id: The task ID.
    :type task_id: str
    :param label_id: The label ID.
    :type label_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def delete_tasks_id_members_id(request: web.Request, user_id, task_id, zap_trace_span=None) -> web.Response:
    """Remove a member from a task

    

    :param user_id: The ID of the member to remove.
    :type user_id: str
    :param task_id: The task ID.
    :type task_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def delete_tasks_id_owners_id(request: web.Request, user_id, task_id, zap_trace_span=None) -> web.Response:
    """Remove an owner from a task

    

    :param user_id: The ID of the owner to remove.
    :type user_id: str
    :param task_id: The task ID.
    :type task_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def delete_tasks_id_runs_id(request: web.Request, task_id, run_id, zap_trace_span=None) -> web.Response:
    """Cancel a running task

    

    :param task_id: The task ID.
    :type task_id: str
    :param run_id: The run ID.
    :type run_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def get_tasks(request: web.Request, zap_trace_span=None, name=None, after=None, user=None, org=None, org_id=None, status=None, limit=None) -> web.Response:
    """List all tasks

    

    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str
    :param name: Returns task with a specific name.
    :type name: str
    :param after: Return tasks after a specified ID.
    :type after: str
    :param user: Filter tasks to a specific user ID.
    :type user: str
    :param org: Filter tasks to a specific organization name.
    :type org: str
    :param org_id: Filter tasks to a specific organization ID.
    :type org_id: str
    :param status: Filter tasks by a status--\&quot;inactive\&quot; or \&quot;active\&quot;.
    :type status: str
    :param limit: The number of tasks to return
    :type limit: int

    """
    return web.Response(status=200)


async def get_tasks_id(request: web.Request, task_id, zap_trace_span=None) -> web.Response:
    """Retrieve a task

    

    :param task_id: The task ID.
    :type task_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def get_tasks_id_labels(request: web.Request, task_id, zap_trace_span=None) -> web.Response:
    """List all labels for a task

    

    :param task_id: The task ID.
    :type task_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def get_tasks_id_logs(request: web.Request, task_id, zap_trace_span=None) -> web.Response:
    """Retrieve all logs for a task

    

    :param task_id: The task ID.
    :type task_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def get_tasks_id_members(request: web.Request, task_id, zap_trace_span=None) -> web.Response:
    """List all task members

    

    :param task_id: The task ID.
    :type task_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def get_tasks_id_owners(request: web.Request, task_id, zap_trace_span=None) -> web.Response:
    """List all owners of a task

    

    :param task_id: The task ID.
    :type task_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def get_tasks_id_runs(request: web.Request, task_id, zap_trace_span=None, after=None, limit=None, after_time=None, before_time=None) -> web.Response:
    """List runs for a task

    

    :param task_id: The ID of the task to get runs for.
    :type task_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str
    :param after: Returns runs after a specific ID.
    :type after: str
    :param limit: The number of runs to return
    :type limit: int
    :param after_time: Filter runs to those scheduled after this time, RFC3339
    :type after_time: str
    :param before_time: Filter runs to those scheduled before this time, RFC3339
    :type before_time: str

    """
    after_time = util.deserialize_datetime(after_time)
    before_time = util.deserialize_datetime(before_time)
    return web.Response(status=200)


async def get_tasks_id_runs_id(request: web.Request, task_id, run_id, zap_trace_span=None) -> web.Response:
    """Retrieve a single run for a task

    

    :param task_id: The task ID.
    :type task_id: str
    :param run_id: The run ID.
    :type run_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def get_tasks_id_runs_id_logs(request: web.Request, task_id, run_id, zap_trace_span=None) -> web.Response:
    """Retrieve all logs for a run

    

    :param task_id: ID of task to get logs for.
    :type task_id: str
    :param run_id: ID of run to get logs for.
    :type run_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def patch_tasks_id(request: web.Request, task_id, body, zap_trace_span=None) -> web.Response:
    """Update a task

    Update a task. This will cancel all queued runs.

    :param task_id: The task ID.
    :type task_id: str
    :param body: Task update to apply
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = TaskUpdateRequest.from_dict(body)
    return web.Response(status=200)


async def post_tasks(request: web.Request, body, zap_trace_span=None) -> web.Response:
    """Create a new task

    

    :param body: Task to create
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = TaskCreateRequest.from_dict(body)
    return web.Response(status=200)


async def post_tasks_id_labels(request: web.Request, task_id, body, zap_trace_span=None) -> web.Response:
    """Add a label to a task

    

    :param task_id: The task ID.
    :type task_id: str
    :param body: Label to add
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = LabelMapping.from_dict(body)
    return web.Response(status=200)


async def post_tasks_id_members(request: web.Request, task_id, body, zap_trace_span=None) -> web.Response:
    """Add a member to a task

    

    :param task_id: The task ID.
    :type task_id: str
    :param body: User to add as member
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = AddResourceMemberRequestBody.from_dict(body)
    return web.Response(status=200)


async def post_tasks_id_owners(request: web.Request, task_id, body, zap_trace_span=None) -> web.Response:
    """Add an owner to a task

    

    :param task_id: The task ID.
    :type task_id: str
    :param body: User to add as owner
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = AddResourceMemberRequestBody.from_dict(body)
    return web.Response(status=200)


async def post_tasks_id_runs(request: web.Request, task_id, zap_trace_span=None, body=None) -> web.Response:
    """Manually start a task run, overriding the current schedule

    

    :param task_id: 
    :type task_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str
    :param body: 
    :type body: dict | bytes

    """
    body = RunManually.from_dict(body)
    return web.Response(status=200)


async def post_tasks_id_runs_id_retry(request: web.Request, task_id, run_id, zap_trace_span=None, body=None) -> web.Response:
    """Retry a task run

    

    :param task_id: The task ID.
    :type task_id: str
    :param run_id: The run ID.
    :type run_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)

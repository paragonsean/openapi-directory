from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_comment_request import AddCommentRequest
from openapi_server.models.edit_task_request import EditTaskRequest
from openapi_server.models.new_task_request import NewTaskRequest
from openapi_server import util


async def add_comment(request: web.Request, accept, content_type, task_id, body) -> web.Response:
    """Add Comment on a Task

    Adds a comment to a given task, filtering by &#x60;taskId&#x60;.

    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param task_id: Task ID.
    :type task_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = AddCommentRequest.from_dict(body)
    return web.Response(status=200)


async def edit_task(request: web.Request, accept, content_type, task_id, body) -> web.Response:
    """Update Task

    Updates a given task&#39;s status, for example, filtering by &#x60;taskId&#x60;.

    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param task_id: Task ID.
    :type task_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = EditTaskRequest.from_dict(body)
    return web.Response(status=200)


async def get_task(request: web.Request, accept, content_type, task_id) -> web.Response:
    """Retrieve Task

    Retrieves a given task, filtering by &#x60;taskId&#x60;.

    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param task_id: Task ID.
    :type task_id: str

    """
    return web.Response(status=200)


async def listtasksbyassignee(request: web.Request, accept, content_type, assignee_email=None, target_id=None, context=None, page=None, per_page=None, status=None) -> web.Response:
    """List tasks

    This endpoint allows you to filter tasks. You can choose between the following filtering options:     - **Assignees:** using &#x60;assignee.email&#x60; and &#x60;status&#x60;. Example: &#x60;https://{{accountName}}.{{environment}}.com.br/api/do/tasks?assignee.email&#x3D;{{person@email.com}}&amp;status&#x3D;{{open}}&#x60;.     - **Targets:** using &#x60;targetId&#x60; and &#x60;status&#x60;. Example: &#x60;https://{{accountName}}.{{environment}}.com.br/api/do/tasks?target.id&#x3D;{{name}}&amp;status&#x3D;{{open}}&#x60;.     - **Paged tasks:** using &#x60;page&#x60;, &#x60;perPage&#x60; and &#x60;status&#x60;. Example: &#x60;https://{{accountName}}.{{environment}}.com.br/api/do/tasks?page&#x3D;{{1}}&amp;perPage&#x3D;{{10}}&amp;status&#x3D;;{{-Closed}}&#x60;.     - **Context:** using &#x60;context&#x60;, &#x60;page&#x60;, &#x60;perPage&#x60; and &#x60;status&#x60;. Example: &#x60;https://{{accountName}}.{{environment}}.com.br/api/do/tasks?context&#x3D;{{context}}&amp;page&#x3D;{{1}}&amp;perPage&#x3D;{{10}}&amp;status&#x3D;{{-Closed}}&#x60;.

    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param assignee_email: If you wish to list tasks by assignee, insert the desired assignee&#39;s email and status.
    :type assignee_email: str
    :param target_id: If you wish to list tasks by target, insert the desired &#x60;targetId&#x60; and &#x60;status&#x60;.
    :type target_id: str
    :param context: If you wish to list tasks by context, insert the desired context, &#x60;page&#x60;, &#x60;perPage&#x60; and &#x60;status&#x60;.
    :type context: str
    :param page: If you wish to list tasks by context, also insert the desired &#x60;page&#x60;.
    :type page: str
    :param per_page: If you wish to list tasks by context, also insert the desired &#x60;perPage&#x60; value.
    :type per_page: str
    :param status: If you wish to list tasks by context, also insert the desired &#x60;status&#x60;.
    :type status: str

    """
    return web.Response(status=200)


async def new_task(request: web.Request, content_type, accept, body) -> web.Response:
    """Create Task

    Creates a new task in VTEX DO.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = NewTaskRequest.from_dict(body)
    return web.Response(status=200)

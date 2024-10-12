from typing import List, Dict
from aiohttp import web

from openapi_server.models.operations_list_default_response import OperationsListDefaultResponse
from openapi_server.models.tasks_get200_response import TasksGet200Response
from openapi_server import util


async def tasks_cancel(request: web.Request, subscription_id, group_name, service_name, project_name, task_name, api_version) -> web.Response:
    """Cancel a task

    The tasks resource is a nested, proxy-only resource representing work performed by a DMS instance. This method cancels a task if it&#39;s currently queued or running.

    :param subscription_id: Identifier of the subscription
    :type subscription_id: str
    :param group_name: Name of the resource group
    :type group_name: str
    :param service_name: Name of the service
    :type service_name: str
    :param project_name: Name of the project
    :type project_name: str
    :param task_name: Name of the Task
    :type task_name: str
    :param api_version: Version of the API
    :type api_version: str

    """
    return web.Response(status=200)


async def tasks_create_or_update(request: web.Request, subscription_id, group_name, service_name, project_name, task_name, api_version, parameters) -> web.Response:
    """Create or update task

    The tasks resource is a nested, proxy-only resource representing work performed by a DMS instance. The PUT method creates a new task or updates an existing one, although since tasks have no mutable custom properties, there is little reason to update an exising one.

    :param subscription_id: Identifier of the subscription
    :type subscription_id: str
    :param group_name: Name of the resource group
    :type group_name: str
    :param service_name: Name of the service
    :type service_name: str
    :param project_name: Name of the project
    :type project_name: str
    :param task_name: Name of the Task
    :type task_name: str
    :param api_version: Version of the API
    :type api_version: str
    :param parameters: Information about the task
    :type parameters: dict | bytes

    """
    parameters = TasksGet200Response.from_dict(parameters)
    return web.Response(status=200)


async def tasks_delete(request: web.Request, subscription_id, group_name, service_name, project_name, task_name, api_version, delete_running_tasks=None) -> web.Response:
    """Delete task

    The tasks resource is a nested, proxy-only resource representing work performed by a DMS instance. The DELETE method deletes a task, canceling it first if it&#39;s running.

    :param subscription_id: Identifier of the subscription
    :type subscription_id: str
    :param group_name: Name of the resource group
    :type group_name: str
    :param service_name: Name of the service
    :type service_name: str
    :param project_name: Name of the project
    :type project_name: str
    :param task_name: Name of the Task
    :type task_name: str
    :param api_version: Version of the API
    :type api_version: str
    :param delete_running_tasks: Delete the resource even if it contains running tasks
    :type delete_running_tasks: bool

    """
    return web.Response(status=200)


async def tasks_get(request: web.Request, subscription_id, group_name, service_name, project_name, task_name, api_version, expand=None) -> web.Response:
    """Get task information

    The tasks resource is a nested, proxy-only resource representing work performed by a DMS instance. The GET method retrieves information about a task.

    :param subscription_id: Identifier of the subscription
    :type subscription_id: str
    :param group_name: Name of the resource group
    :type group_name: str
    :param service_name: Name of the service
    :type service_name: str
    :param project_name: Name of the project
    :type project_name: str
    :param task_name: Name of the Task
    :type task_name: str
    :param api_version: Version of the API
    :type api_version: str
    :param expand: Expand the response
    :type expand: str

    """
    return web.Response(status=200)


async def tasks_update(request: web.Request, subscription_id, group_name, service_name, project_name, task_name, api_version, parameters) -> web.Response:
    """Create or update task

    The tasks resource is a nested, proxy-only resource representing work performed by a DMS instance. The PATCH method updates an existing task, but since tasks have no mutable custom properties, there is little reason to do so.

    :param subscription_id: Identifier of the subscription
    :type subscription_id: str
    :param group_name: Name of the resource group
    :type group_name: str
    :param service_name: Name of the service
    :type service_name: str
    :param project_name: Name of the project
    :type project_name: str
    :param task_name: Name of the Task
    :type task_name: str
    :param api_version: Version of the API
    :type api_version: str
    :param parameters: Information about the task
    :type parameters: dict | bytes

    """
    parameters = TasksGet200Response.from_dict(parameters)
    return web.Response(status=200)

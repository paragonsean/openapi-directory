from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_schema import ErrorSchema
from openapi_server.models.task import Task
from openapi_server.models.task_list_result import TaskListResult
from openapi_server.models.task_update_parameters import TaskUpdateParameters
from openapi_server import util


async def tasks_create(request: web.Request, subscription_id, resource_group_name, registry_name, api_version, task_name, task_create_parameters) -> web.Response:
    """tasks_create

    Creates a task for a container registry with the specified parameters.

    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the container registry belongs.
    :type resource_group_name: str
    :param registry_name: The name of the container registry.
    :type registry_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param task_name: The name of the container registry task.
    :type task_name: str
    :param task_create_parameters: The parameters for creating a task.
    :type task_create_parameters: dict | bytes

    """
    task_create_parameters = Task.from_dict(task_create_parameters)
    return web.Response(status=200)


async def tasks_delete(request: web.Request, subscription_id, resource_group_name, registry_name, api_version, task_name) -> web.Response:
    """tasks_delete

    Deletes a specified task.

    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the container registry belongs.
    :type resource_group_name: str
    :param registry_name: The name of the container registry.
    :type registry_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param task_name: The name of the container registry task.
    :type task_name: str

    """
    return web.Response(status=200)


async def tasks_get(request: web.Request, subscription_id, resource_group_name, registry_name, api_version, task_name) -> web.Response:
    """tasks_get

    Get the properties of a specified task.

    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the container registry belongs.
    :type resource_group_name: str
    :param registry_name: The name of the container registry.
    :type registry_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param task_name: The name of the container registry task.
    :type task_name: str

    """
    return web.Response(status=200)


async def tasks_get_details(request: web.Request, subscription_id, resource_group_name, registry_name, api_version, task_name) -> web.Response:
    """tasks_get_details

    Returns a task with extended information that includes all secrets.

    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the container registry belongs.
    :type resource_group_name: str
    :param registry_name: The name of the container registry.
    :type registry_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param task_name: The name of the container registry task.
    :type task_name: str

    """
    return web.Response(status=200)


async def tasks_list(request: web.Request, subscription_id, resource_group_name, registry_name, api_version) -> web.Response:
    """tasks_list

    Lists all the tasks for a specified container registry.

    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the container registry belongs.
    :type resource_group_name: str
    :param registry_name: The name of the container registry.
    :type registry_name: str
    :param api_version: The client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def tasks_update(request: web.Request, subscription_id, resource_group_name, registry_name, api_version, task_name, task_update_parameters) -> web.Response:
    """tasks_update

    Updates a task with the specified parameters.

    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the container registry belongs.
    :type resource_group_name: str
    :param registry_name: The name of the container registry.
    :type registry_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param task_name: The name of the container registry task.
    :type task_name: str
    :param task_update_parameters: The parameters for updating a task.
    :type task_update_parameters: dict | bytes

    """
    task_update_parameters = TaskUpdateParameters.from_dict(task_update_parameters)
    return web.Response(status=200)

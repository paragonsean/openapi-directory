from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_schema import ErrorSchema
from openapi_server.models.task_run import TaskRun
from openapi_server.models.task_run_list_result import TaskRunListResult
from openapi_server.models.task_run_update_parameters import TaskRunUpdateParameters
from openapi_server import util


async def task_runs_create(request: web.Request, subscription_id, resource_group_name, registry_name, api_version, task_run_name, task_run) -> web.Response:
    """task_runs_create

    Creates a task run for a container registry with the specified parameters.

    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the container registry belongs.
    :type resource_group_name: str
    :param registry_name: The name of the container registry.
    :type registry_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param task_run_name: The name of task run.
    :type task_run_name: str
    :param task_run: The parameters of a run that needs to scheduled.
    :type task_run: dict | bytes

    """
    task_run = TaskRun.from_dict(task_run)
    return web.Response(status=200)


async def task_runs_delete(request: web.Request, subscription_id, resource_group_name, registry_name, api_version, task_run_name) -> web.Response:
    """task_runs_delete

    Deletes a specified task run resource.

    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the container registry belongs.
    :type resource_group_name: str
    :param registry_name: The name of the container registry.
    :type registry_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param task_run_name: The task run name.
    :type task_run_name: str

    """
    return web.Response(status=200)


async def task_runs_get(request: web.Request, subscription_id, resource_group_name, registry_name, api_version, task_run_name) -> web.Response:
    """task_runs_get

    Gets the detailed information for a given task run.

    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the container registry belongs.
    :type resource_group_name: str
    :param registry_name: The name of the container registry.
    :type registry_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param task_run_name: The run request name.
    :type task_run_name: str

    """
    return web.Response(status=200)


async def task_runs_list(request: web.Request, subscription_id, resource_group_name, registry_name, api_version) -> web.Response:
    """task_runs_list

    Lists all the task runs for a specified container registry.

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


async def task_runs_update(request: web.Request, subscription_id, resource_group_name, registry_name, api_version, task_run_name, update_parameters) -> web.Response:
    """task_runs_update

    Updates a task run with the specified parameters.

    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the container registry belongs.
    :type resource_group_name: str
    :param registry_name: The name of the container registry.
    :type registry_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param task_run_name: The task run name.
    :type task_run_name: str
    :param update_parameters: The parameters for updating a task run.
    :type update_parameters: dict | bytes

    """
    update_parameters = TaskRunUpdateParameters.from_dict(update_parameters)
    return web.Response(status=200)

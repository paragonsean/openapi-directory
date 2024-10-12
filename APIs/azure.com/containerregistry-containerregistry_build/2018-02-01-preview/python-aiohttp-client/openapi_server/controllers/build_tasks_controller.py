from typing import List, Dict
from aiohttp import web

from openapi_server.models.build_task import BuildTask
from openapi_server.models.build_task_list_result import BuildTaskListResult
from openapi_server.models.build_task_update_parameters import BuildTaskUpdateParameters
from openapi_server.models.source_repository_properties import SourceRepositoryProperties
from openapi_server import util


async def build_tasks_create(request: web.Request, subscription_id, resource_group_name, registry_name, api_version, build_task_name, build_task_create_parameters) -> web.Response:
    """build_tasks_create

    Creates a build task for a container registry with the specified parameters.

    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the container registry belongs.
    :type resource_group_name: str
    :param registry_name: The name of the container registry.
    :type registry_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param build_task_name: The name of the container registry build task.
    :type build_task_name: str
    :param build_task_create_parameters: The parameters for creating a build task.
    :type build_task_create_parameters: dict | bytes

    """
    build_task_create_parameters = BuildTask.from_dict(build_task_create_parameters)
    return web.Response(status=200)


async def build_tasks_delete(request: web.Request, subscription_id, resource_group_name, registry_name, api_version, build_task_name) -> web.Response:
    """build_tasks_delete

    Deletes a specified build task.

    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the container registry belongs.
    :type resource_group_name: str
    :param registry_name: The name of the container registry.
    :type registry_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param build_task_name: The name of the container registry build task.
    :type build_task_name: str

    """
    return web.Response(status=200)


async def build_tasks_get(request: web.Request, subscription_id, resource_group_name, registry_name, api_version, build_task_name) -> web.Response:
    """build_tasks_get

    Get the properties of a specified build task.

    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the container registry belongs.
    :type resource_group_name: str
    :param registry_name: The name of the container registry.
    :type registry_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param build_task_name: The name of the container registry build task.
    :type build_task_name: str

    """
    return web.Response(status=200)


async def build_tasks_list(request: web.Request, subscription_id, resource_group_name, registry_name, api_version, filter=None, skip_token=None) -> web.Response:
    """build_tasks_list

    Lists all the build tasks for a specified container registry.

    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the container registry belongs.
    :type resource_group_name: str
    :param registry_name: The name of the container registry.
    :type registry_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param filter: The build task filter to apply on the operation.
    :type filter: str
    :param skip_token: $skipToken is supported on get list of build tasks, which provides the next page in the list of tasks.
    :type skip_token: str

    """
    return web.Response(status=200)


async def build_tasks_list_source_repository_properties(request: web.Request, subscription_id, resource_group_name, registry_name, api_version, build_task_name) -> web.Response:
    """build_tasks_list_source_repository_properties

    Get the source control properties for a build task.

    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the container registry belongs.
    :type resource_group_name: str
    :param registry_name: The name of the container registry.
    :type registry_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param build_task_name: The name of the container registry build task.
    :type build_task_name: str

    """
    return web.Response(status=200)


async def build_tasks_update(request: web.Request, subscription_id, resource_group_name, registry_name, api_version, build_task_name, build_task_update_parameters) -> web.Response:
    """build_tasks_update

    Updates a build task with the specified parameters.

    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the container registry belongs.
    :type resource_group_name: str
    :param registry_name: The name of the container registry.
    :type registry_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param build_task_name: The name of the container registry build task.
    :type build_task_name: str
    :param build_task_update_parameters: The parameters for updating a build task.
    :type build_task_update_parameters: dict | bytes

    """
    build_task_update_parameters = BuildTaskUpdateParameters.from_dict(build_task_update_parameters)
    return web.Response(status=200)

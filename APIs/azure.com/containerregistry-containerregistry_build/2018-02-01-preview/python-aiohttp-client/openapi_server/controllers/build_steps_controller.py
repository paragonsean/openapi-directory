from typing import List, Dict
from aiohttp import web

from openapi_server.models.build_argument_list import BuildArgumentList
from openapi_server.models.build_step import BuildStep
from openapi_server.models.build_step_list import BuildStepList
from openapi_server.models.build_step_update_parameters import BuildStepUpdateParameters
from openapi_server import util


async def build_steps_create(request: web.Request, subscription_id, resource_group_name, registry_name, api_version, build_task_name, step_name, build_step_create_parameters) -> web.Response:
    """build_steps_create

    Creates a build step for a build task.

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
    :param step_name: The name of a build step for a container registry build task.
    :type step_name: str
    :param build_step_create_parameters: The parameters for creating a build step.
    :type build_step_create_parameters: dict | bytes

    """
    build_step_create_parameters = BuildStep.from_dict(build_step_create_parameters)
    return web.Response(status=200)


async def build_steps_delete(request: web.Request, subscription_id, resource_group_name, registry_name, api_version, build_task_name, step_name) -> web.Response:
    """build_steps_delete

    Deletes a build step from the build task.

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
    :param step_name: The name of a build step for a container registry build task.
    :type step_name: str

    """
    return web.Response(status=200)


async def build_steps_get(request: web.Request, subscription_id, resource_group_name, registry_name, api_version, build_task_name, step_name) -> web.Response:
    """build_steps_get

    Gets the build step for a build task.

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
    :param step_name: The name of a build step for a container registry build task.
    :type step_name: str

    """
    return web.Response(status=200)


async def build_steps_list(request: web.Request, subscription_id, resource_group_name, registry_name, api_version, build_task_name) -> web.Response:
    """build_steps_list

    List all the build steps for a given build task.

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


async def build_steps_list_build_arguments(request: web.Request, subscription_id, resource_group_name, registry_name, api_version, build_task_name, step_name) -> web.Response:
    """build_steps_list_build_arguments

    List the build arguments for a step including the secret arguments.

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
    :param step_name: The name of a build step for a container registry build task.
    :type step_name: str

    """
    return web.Response(status=200)


async def build_steps_update(request: web.Request, subscription_id, resource_group_name, registry_name, api_version, build_task_name, step_name, build_step_update_parameters) -> web.Response:
    """build_steps_update

    Updates a build step in a build task.

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
    :param step_name: The name of a build step for a container registry build task.
    :type step_name: str
    :param build_step_update_parameters: The parameters for updating a build step.
    :type build_step_update_parameters: dict | bytes

    """
    build_step_update_parameters = BuildStepUpdateParameters.from_dict(build_step_update_parameters)
    return web.Response(status=200)

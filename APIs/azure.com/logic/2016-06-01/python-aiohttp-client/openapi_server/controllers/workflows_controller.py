from typing import List, Dict
from aiohttp import web

from openapi_server.models.generate_upgraded_definition_parameters import GenerateUpgradedDefinitionParameters
from openapi_server.models.get_callback_url_parameters import GetCallbackUrlParameters
from openapi_server.models.regenerate_action_parameter import RegenerateActionParameter
from openapi_server.models.workflow import Workflow
from openapi_server.models.workflow_list_result import WorkflowListResult
from openapi_server.models.workflow_trigger_callback_url import WorkflowTriggerCallbackUrl
from openapi_server import util


async def workflows_create_or_update(request: web.Request, subscription_id, resource_group_name, workflow_name, api_version, workflow) -> web.Response:
    """workflows_create_or_update

    Creates or updates a workflow.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param workflow_name: The workflow name.
    :type workflow_name: str
    :param api_version: The API version.
    :type api_version: str
    :param workflow: The workflow.
    :type workflow: dict | bytes

    """
    workflow = Workflow.from_dict(workflow)
    return web.Response(status=200)


async def workflows_delete(request: web.Request, subscription_id, resource_group_name, workflow_name, api_version) -> web.Response:
    """workflows_delete

    Deletes a workflow.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param workflow_name: The workflow name.
    :type workflow_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def workflows_disable(request: web.Request, subscription_id, resource_group_name, workflow_name, api_version) -> web.Response:
    """workflows_disable

    Disables a workflow.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param workflow_name: The workflow name.
    :type workflow_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def workflows_enable(request: web.Request, subscription_id, resource_group_name, workflow_name, api_version) -> web.Response:
    """workflows_enable

    Enables a workflow.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param workflow_name: The workflow name.
    :type workflow_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def workflows_generate_upgraded_definition(request: web.Request, subscription_id, resource_group_name, workflow_name, api_version, parameters) -> web.Response:
    """workflows_generate_upgraded_definition

    Generates the upgraded definition for a workflow.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param workflow_name: The workflow name.
    :type workflow_name: str
    :param api_version: The API version.
    :type api_version: str
    :param parameters: Parameters for generating an upgraded definition.
    :type parameters: dict | bytes

    """
    parameters = GenerateUpgradedDefinitionParameters.from_dict(parameters)
    return web.Response(status=200)


async def workflows_get(request: web.Request, subscription_id, resource_group_name, workflow_name, api_version) -> web.Response:
    """workflows_get

    Gets a workflow.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param workflow_name: The workflow name.
    :type workflow_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def workflows_list_by_resource_group(request: web.Request, subscription_id, resource_group_name, api_version, top=None, filter=None) -> web.Response:
    """workflows_list_by_resource_group

    Gets a list of workflows by resource group.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param api_version: The API version.
    :type api_version: str
    :param top: The number of items to be included in the result.
    :type top: int
    :param filter: The filter to apply on the operation. Options for filters include: State, Trigger, and ReferencedResourceId.
    :type filter: str

    """
    return web.Response(status=200)


async def workflows_list_by_subscription(request: web.Request, subscription_id, api_version, top=None, filter=None) -> web.Response:
    """workflows_list_by_subscription

    Gets a list of workflows by subscription.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param api_version: The API version.
    :type api_version: str
    :param top: The number of items to be included in the result.
    :type top: int
    :param filter: The filter to apply on the operation. Options for filters include: State, Trigger, and ReferencedResourceId.
    :type filter: str

    """
    return web.Response(status=200)


async def workflows_list_callback_url(request: web.Request, subscription_id, resource_group_name, workflow_name, api_version, list_callback_url) -> web.Response:
    """workflows_list_callback_url

    Get the workflow callback Url.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param workflow_name: The workflow name.
    :type workflow_name: str
    :param api_version: The API version.
    :type api_version: str
    :param list_callback_url: Which callback url to list.
    :type list_callback_url: dict | bytes

    """
    list_callback_url = GetCallbackUrlParameters.from_dict(list_callback_url)
    return web.Response(status=200)


async def workflows_list_swagger(request: web.Request, subscription_id, resource_group_name, workflow_name, api_version) -> web.Response:
    """workflows_list_swagger

    Gets an OpenAPI definition for the workflow.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param workflow_name: The workflow name.
    :type workflow_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def workflows_move(request: web.Request, subscription_id, resource_group_name, workflow_name, api_version, move) -> web.Response:
    """workflows_move

    Moves an existing workflow.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param workflow_name: The workflow name.
    :type workflow_name: str
    :param api_version: The API version.
    :type api_version: str
    :param move: The workflow to move.
    :type move: dict | bytes

    """
    move = Workflow.from_dict(move)
    return web.Response(status=200)


async def workflows_regenerate_access_key(request: web.Request, subscription_id, resource_group_name, workflow_name, api_version, key_type) -> web.Response:
    """workflows_regenerate_access_key

    Regenerates the callback URL access key for request triggers.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param workflow_name: The workflow name.
    :type workflow_name: str
    :param api_version: The API version.
    :type api_version: str
    :param key_type: The access key type.
    :type key_type: dict | bytes

    """
    key_type = RegenerateActionParameter.from_dict(key_type)
    return web.Response(status=200)


async def workflows_update(request: web.Request, subscription_id, resource_group_name, workflow_name, api_version, workflow) -> web.Response:
    """workflows_update

    Updates a workflow.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param workflow_name: The workflow name.
    :type workflow_name: str
    :param api_version: The API version.
    :type api_version: str
    :param workflow: The workflow.
    :type workflow: dict | bytes

    """
    workflow = Workflow.from_dict(workflow)
    return web.Response(status=200)


async def workflows_validate(request: web.Request, subscription_id, resource_group_name, location, workflow_name, api_version, workflow) -> web.Response:
    """workflows_validate

    Validates the workflow definition.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param location: The workflow location.
    :type location: str
    :param workflow_name: The workflow name.
    :type workflow_name: str
    :param api_version: The API version.
    :type api_version: str
    :param workflow: The workflow definition.
    :type workflow: dict | bytes

    """
    workflow = Workflow.from_dict(workflow)
    return web.Response(status=200)


async def workflows_validate_workflow(request: web.Request, subscription_id, resource_group_name, workflow_name, api_version, validate) -> web.Response:
    """workflows_validate_workflow

    Validates the workflow.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param workflow_name: The workflow name.
    :type workflow_name: str
    :param api_version: The API version.
    :type api_version: str
    :param validate: The workflow.
    :type validate: dict | bytes

    """
    validate = Workflow.from_dict(validate)
    return web.Response(status=200)

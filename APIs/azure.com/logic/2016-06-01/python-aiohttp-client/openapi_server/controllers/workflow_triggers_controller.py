from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_callback_url_parameters import GetCallbackUrlParameters
from openapi_server.models.json_schema import JsonSchema
from openapi_server.models.set_trigger_state_action_definition import SetTriggerStateActionDefinition
from openapi_server.models.workflow_trigger import WorkflowTrigger
from openapi_server.models.workflow_trigger_callback_url import WorkflowTriggerCallbackUrl
from openapi_server.models.workflow_trigger_list_result import WorkflowTriggerListResult
from openapi_server import util


async def workflow_triggers_get(request: web.Request, subscription_id, resource_group_name, workflow_name, trigger_name, api_version) -> web.Response:
    """workflow_triggers_get

    Gets a workflow trigger.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param workflow_name: The workflow name.
    :type workflow_name: str
    :param trigger_name: The workflow trigger name.
    :type trigger_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def workflow_triggers_get_schema_json(request: web.Request, subscription_id, resource_group_name, workflow_name, trigger_name, api_version) -> web.Response:
    """workflow_triggers_get_schema_json

    Get the trigger schema as JSON.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param workflow_name: The workflow name.
    :type workflow_name: str
    :param trigger_name: The workflow trigger name.
    :type trigger_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def workflow_triggers_list(request: web.Request, subscription_id, resource_group_name, workflow_name, api_version, top=None, filter=None) -> web.Response:
    """workflow_triggers_list

    Gets a list of workflow triggers.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param workflow_name: The workflow name.
    :type workflow_name: str
    :param api_version: The API version.
    :type api_version: str
    :param top: The number of items to be included in the result.
    :type top: int
    :param filter: The filter to apply on the operation.
    :type filter: str

    """
    return web.Response(status=200)


async def workflow_triggers_list_callback_url(request: web.Request, subscription_id, resource_group_name, workflow_name, trigger_name, api_version) -> web.Response:
    """workflow_triggers_list_callback_url

    Get the callback URL for a workflow trigger.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param workflow_name: The workflow name.
    :type workflow_name: str
    :param trigger_name: The workflow trigger name.
    :type trigger_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def workflow_triggers_reset(request: web.Request, subscription_id, resource_group_name, workflow_name, trigger_name, api_version) -> web.Response:
    """workflow_triggers_reset

    Resets a workflow trigger.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param workflow_name: The workflow name.
    :type workflow_name: str
    :param trigger_name: The workflow trigger name.
    :type trigger_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def workflow_triggers_run(request: web.Request, subscription_id, resource_group_name, workflow_name, trigger_name, api_version) -> web.Response:
    """workflow_triggers_run

    Runs a workflow trigger.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param workflow_name: The workflow name.
    :type workflow_name: str
    :param trigger_name: The workflow trigger name.
    :type trigger_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def workflow_triggers_set_state(request: web.Request, subscription_id, resource_group_name, workflow_name, trigger_name, api_version, set_state) -> web.Response:
    """workflow_triggers_set_state

    Sets the state of a workflow trigger.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param workflow_name: The workflow name.
    :type workflow_name: str
    :param trigger_name: The workflow trigger name.
    :type trigger_name: str
    :param api_version: The API version.
    :type api_version: str
    :param set_state: The workflow trigger state.
    :type set_state: dict | bytes

    """
    set_state = SetTriggerStateActionDefinition.from_dict(set_state)
    return web.Response(status=200)


async def workflow_versions_list_callback_url(request: web.Request, subscription_id, resource_group_name, workflow_name, version_id, trigger_name, api_version, parameters=None) -> web.Response:
    """workflow_versions_list_callback_url

    Get the callback url for a trigger of a workflow version.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param workflow_name: The workflow name.
    :type workflow_name: str
    :param version_id: The workflow versionId.
    :type version_id: str
    :param trigger_name: The workflow trigger name.
    :type trigger_name: str
    :param api_version: The API version.
    :type api_version: str
    :param parameters: The callback URL parameters.
    :type parameters: dict | bytes

    """
    parameters = GetCallbackUrlParameters.from_dict(parameters)
    return web.Response(status=200)

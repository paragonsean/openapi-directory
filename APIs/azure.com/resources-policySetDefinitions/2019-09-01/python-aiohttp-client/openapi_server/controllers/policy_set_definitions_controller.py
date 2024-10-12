from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.policy_set_definition import PolicySetDefinition
from openapi_server.models.policy_set_definition_list_result import PolicySetDefinitionListResult
from openapi_server import util


async def policy_set_definitions_create_or_update(request: web.Request, policy_set_definition_name, api_version, subscription_id, parameters) -> web.Response:
    """Creates or updates a policy set definition.

    This operation creates or updates a policy set definition in the given subscription with the given name.

    :param policy_set_definition_name: The name of the policy set definition to create.
    :type policy_set_definition_name: str
    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param parameters: The policy set definition properties.
    :type parameters: dict | bytes

    """
    parameters = PolicySetDefinition.from_dict(parameters)
    return web.Response(status=200)


async def policy_set_definitions_create_or_update_at_management_group(request: web.Request, policy_set_definition_name, api_version, management_group_id, parameters) -> web.Response:
    """Creates or updates a policy set definition.

    This operation creates or updates a policy set definition in the given management group with the given name.

    :param policy_set_definition_name: The name of the policy set definition to create.
    :type policy_set_definition_name: str
    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param management_group_id: The ID of the management group.
    :type management_group_id: str
    :param parameters: The policy set definition properties.
    :type parameters: dict | bytes

    """
    parameters = PolicySetDefinition.from_dict(parameters)
    return web.Response(status=200)


async def policy_set_definitions_delete(request: web.Request, policy_set_definition_name, api_version, subscription_id) -> web.Response:
    """Deletes a policy set definition.

    This operation deletes the policy set definition in the given subscription with the given name.

    :param policy_set_definition_name: The name of the policy set definition to delete.
    :type policy_set_definition_name: str
    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def policy_set_definitions_delete_at_management_group(request: web.Request, policy_set_definition_name, api_version, management_group_id) -> web.Response:
    """Deletes a policy set definition.

    This operation deletes the policy set definition in the given management group with the given name.

    :param policy_set_definition_name: The name of the policy set definition to delete.
    :type policy_set_definition_name: str
    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param management_group_id: The ID of the management group.
    :type management_group_id: str

    """
    return web.Response(status=200)


async def policy_set_definitions_get(request: web.Request, policy_set_definition_name, api_version, subscription_id) -> web.Response:
    """Retrieves a policy set definition.

    This operation retrieves the policy set definition in the given subscription with the given name.

    :param policy_set_definition_name: The name of the policy set definition to get.
    :type policy_set_definition_name: str
    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def policy_set_definitions_get_at_management_group(request: web.Request, policy_set_definition_name, api_version, management_group_id) -> web.Response:
    """Retrieves a policy set definition.

    This operation retrieves the policy set definition in the given management group with the given name.

    :param policy_set_definition_name: The name of the policy set definition to get.
    :type policy_set_definition_name: str
    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param management_group_id: The ID of the management group.
    :type management_group_id: str

    """
    return web.Response(status=200)


async def policy_set_definitions_get_built_in(request: web.Request, policy_set_definition_name, api_version) -> web.Response:
    """Retrieves a built in policy set definition.

    This operation retrieves the built-in policy set definition with the given name.

    :param policy_set_definition_name: The name of the policy set definition to get.
    :type policy_set_definition_name: str
    :param api_version: The API version to use for the operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def policy_set_definitions_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """Retrieves the policy set definitions for a subscription.

    This operation retrieves a list of all the policy set definitions in the given subscription.

    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def policy_set_definitions_list_built_in(request: web.Request, api_version) -> web.Response:
    """Retrieves built-in policy set definitions.

    This operation retrieves a list of all the built-in policy set definitions.

    :param api_version: The API version to use for the operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def policy_set_definitions_list_by_management_group(request: web.Request, api_version, management_group_id) -> web.Response:
    """Retrieves all policy set definitions in management group.

    This operation retrieves a list of all the a policy set definition in the given management group.

    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param management_group_id: The ID of the management group.
    :type management_group_id: str

    """
    return web.Response(status=200)

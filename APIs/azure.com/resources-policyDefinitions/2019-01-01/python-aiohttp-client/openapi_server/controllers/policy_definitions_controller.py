from typing import List, Dict
from aiohttp import web

from openapi_server.models.policy_definition import PolicyDefinition
from openapi_server.models.policy_definition_list_result import PolicyDefinitionListResult
from openapi_server import util


async def policy_definitions_create_or_update(request: web.Request, policy_definition_name, api_version, subscription_id, parameters) -> web.Response:
    """Creates or updates a policy definition in a subscription.

    This operation creates or updates a policy definition in the given subscription with the given name.

    :param policy_definition_name: The name of the policy definition to create.
    :type policy_definition_name: str
    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param parameters: The policy definition properties.
    :type parameters: dict | bytes

    """
    parameters = PolicyDefinition.from_dict(parameters)
    return web.Response(status=200)


async def policy_definitions_create_or_update_at_management_group(request: web.Request, policy_definition_name, api_version, management_group_id, parameters) -> web.Response:
    """Creates or updates a policy definition in a management group.

    This operation creates or updates a policy definition in the given management group with the given name.

    :param policy_definition_name: The name of the policy definition to create.
    :type policy_definition_name: str
    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param management_group_id: The ID of the management group.
    :type management_group_id: str
    :param parameters: The policy definition properties.
    :type parameters: dict | bytes

    """
    parameters = PolicyDefinition.from_dict(parameters)
    return web.Response(status=200)


async def policy_definitions_delete(request: web.Request, policy_definition_name, api_version, subscription_id) -> web.Response:
    """Deletes a policy definition in a subscription.

    This operation deletes the policy definition in the given subscription with the given name.

    :param policy_definition_name: The name of the policy definition to delete.
    :type policy_definition_name: str
    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def policy_definitions_delete_at_management_group(request: web.Request, policy_definition_name, api_version, management_group_id) -> web.Response:
    """Deletes a policy definition in a management group.

    This operation deletes the policy definition in the given management group with the given name.

    :param policy_definition_name: The name of the policy definition to delete.
    :type policy_definition_name: str
    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param management_group_id: The ID of the management group.
    :type management_group_id: str

    """
    return web.Response(status=200)


async def policy_definitions_get(request: web.Request, policy_definition_name, api_version, subscription_id) -> web.Response:
    """Retrieves a policy definition in a subscription.

    This operation retrieves the policy definition in the given subscription with the given name.

    :param policy_definition_name: The name of the policy definition to get.
    :type policy_definition_name: str
    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def policy_definitions_get_at_management_group(request: web.Request, policy_definition_name, api_version, management_group_id) -> web.Response:
    """Retrieve a policy definition in a management group.

    This operation retrieves the policy definition in the given management group with the given name.

    :param policy_definition_name: The name of the policy definition to get.
    :type policy_definition_name: str
    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param management_group_id: The ID of the management group.
    :type management_group_id: str

    """
    return web.Response(status=200)


async def policy_definitions_get_built_in(request: web.Request, policy_definition_name, api_version) -> web.Response:
    """Retrieves a built-in policy definition.

    This operation retrieves the built-in policy definition with the given name.

    :param policy_definition_name: The name of the built-in policy definition to get.
    :type policy_definition_name: str
    :param api_version: The API version to use for the operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def policy_definitions_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """Retrieves policy definitions in a subscription

    This operation retrieves a list of all the policy definitions in a given subscription.

    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def policy_definitions_list_built_in(request: web.Request, api_version) -> web.Response:
    """Retrieve built-in policy definitions

    This operation retrieves a list of all the built-in policy definitions.

    :param api_version: The API version to use for the operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def policy_definitions_list_by_management_group(request: web.Request, api_version, management_group_id) -> web.Response:
    """Retrieve policy definitions in a management group

    This operation retrieves a list of all the policy definitions in a given management group.

    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param management_group_id: The ID of the management group.
    :type management_group_id: str

    """
    return web.Response(status=200)

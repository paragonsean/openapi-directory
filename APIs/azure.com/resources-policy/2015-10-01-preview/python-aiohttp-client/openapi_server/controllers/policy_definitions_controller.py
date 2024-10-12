from typing import List, Dict
from aiohttp import web

from openapi_server.models.policy_definition import PolicyDefinition
from openapi_server.models.policy_definition_list_result import PolicyDefinitionListResult
from openapi_server import util


async def policy_definitions_create_or_update(request: web.Request, policy_definition_name, api_version, subscription_id, parameters) -> web.Response:
    """policy_definitions_create_or_update

    Creates or updates a policy definition.

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


async def policy_definitions_delete(request: web.Request, policy_definition_name, api_version, subscription_id) -> web.Response:
    """policy_definitions_delete

    Deletes a policy definition.

    :param policy_definition_name: The name of the policy definition to delete.
    :type policy_definition_name: str
    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def policy_definitions_get(request: web.Request, policy_definition_name, api_version, subscription_id) -> web.Response:
    """policy_definitions_get

    Gets the policy definition.

    :param policy_definition_name: The name of the policy definition to get.
    :type policy_definition_name: str
    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def policy_definitions_list(request: web.Request, api_version, subscription_id, filter=None) -> web.Response:
    """policy_definitions_list

    Gets all the policy definitions for a subscription.

    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param filter: The filter to apply on the operation.
    :type filter: str

    """
    return web.Response(status=200)

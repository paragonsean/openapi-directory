from typing import List, Dict
from aiohttp import web

from openapi_server.models.authorization_policy import AuthorizationPolicy
from openapi_server.models.authorization_policy_list_result import AuthorizationPolicyListResult
from openapi_server.models.authorization_policy_resource_format import AuthorizationPolicyResourceFormat
from openapi_server import util


async def authorization_policies_create_or_update(request: web.Request, resource_group_name, hub_name, authorization_policy_name, api_version, subscription_id, parameters) -> web.Response:
    """authorization_policies_create_or_update

    Creates an authorization policy or updates an existing authorization policy.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param hub_name: The name of the hub.
    :type hub_name: str
    :param authorization_policy_name: The name of the policy.
    :type authorization_policy_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the CreateOrUpdate authorization policy operation.
    :type parameters: dict | bytes

    """
    parameters = AuthorizationPolicyResourceFormat.from_dict(parameters)
    return web.Response(status=200)


async def authorization_policies_get(request: web.Request, resource_group_name, hub_name, authorization_policy_name, api_version, subscription_id) -> web.Response:
    """authorization_policies_get

    Gets an authorization policy in the hub.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param hub_name: The name of the hub.
    :type hub_name: str
    :param authorization_policy_name: The name of the policy.
    :type authorization_policy_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def authorization_policies_list_by_hub(request: web.Request, resource_group_name, hub_name, api_version, subscription_id) -> web.Response:
    """authorization_policies_list_by_hub

    Gets all the authorization policies in a specified hub.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param hub_name: The name of the hub.
    :type hub_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def authorization_policies_regenerate_primary_key(request: web.Request, resource_group_name, hub_name, authorization_policy_name, api_version, subscription_id) -> web.Response:
    """authorization_policies_regenerate_primary_key

    Regenerates the primary policy key of the specified authorization policy.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param hub_name: The name of the hub.
    :type hub_name: str
    :param authorization_policy_name: The name of the policy.
    :type authorization_policy_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def authorization_policies_regenerate_secondary_key(request: web.Request, resource_group_name, hub_name, authorization_policy_name, api_version, subscription_id) -> web.Response:
    """authorization_policies_regenerate_secondary_key

    Regenerates the secondary policy key of the specified authorization policy.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param hub_name: The name of the hub.
    :type hub_name: str
    :param authorization_policy_name: The name of the policy.
    :type authorization_policy_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)

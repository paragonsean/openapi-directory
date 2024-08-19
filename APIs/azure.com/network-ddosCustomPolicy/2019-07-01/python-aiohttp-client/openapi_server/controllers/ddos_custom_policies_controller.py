from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.ddos_custom_policies_update_tags_request import DdosCustomPoliciesUpdateTagsRequest
from openapi_server.models.ddos_custom_policy import DdosCustomPolicy
from openapi_server import util


async def ddos_custom_policies_create_or_update(request: web.Request, resource_group_name, ddos_custom_policy_name, api_version, subscription_id, parameters) -> web.Response:
    """ddos_custom_policies_create_or_update

    Creates or updates a DDoS custom policy.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param ddos_custom_policy_name: The name of the DDoS custom policy.
    :type ddos_custom_policy_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the create or update operation.
    :type parameters: dict | bytes

    """
    parameters = DdosCustomPolicy.from_dict(parameters)
    return web.Response(status=200)


async def ddos_custom_policies_delete(request: web.Request, resource_group_name, ddos_custom_policy_name, api_version, subscription_id) -> web.Response:
    """ddos_custom_policies_delete

    Deletes the specified DDoS custom policy.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param ddos_custom_policy_name: The name of the DDoS custom policy.
    :type ddos_custom_policy_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def ddos_custom_policies_get(request: web.Request, resource_group_name, ddos_custom_policy_name, api_version, subscription_id) -> web.Response:
    """ddos_custom_policies_get

    Gets information about the specified DDoS custom policy.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param ddos_custom_policy_name: The name of the DDoS custom policy.
    :type ddos_custom_policy_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def ddos_custom_policies_update_tags(request: web.Request, resource_group_name, ddos_custom_policy_name, api_version, subscription_id, parameters) -> web.Response:
    """ddos_custom_policies_update_tags

    Update a DDoS custom policy tags.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param ddos_custom_policy_name: The name of the DDoS custom policy.
    :type ddos_custom_policy_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the update DDoS custom policy resource tags.
    :type parameters: dict | bytes

    """
    parameters = DdosCustomPoliciesUpdateTagsRequest.from_dict(parameters)
    return web.Response(status=200)

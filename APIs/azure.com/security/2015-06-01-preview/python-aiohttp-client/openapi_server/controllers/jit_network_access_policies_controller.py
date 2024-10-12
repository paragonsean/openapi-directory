from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.jit_network_access_policies_list import JitNetworkAccessPoliciesList
from openapi_server.models.jit_network_access_policy import JitNetworkAccessPolicy
from openapi_server.models.jit_network_access_policy_initiate_request import JitNetworkAccessPolicyInitiateRequest
from openapi_server.models.jit_network_access_request import JitNetworkAccessRequest
from openapi_server import util


async def jit_network_access_policies_create_or_update(request: web.Request, subscription_id, resource_group_name, asc_location, jit_network_access_policy_name, api_version, body) -> web.Response:
    """jit_network_access_policies_create_or_update

    Create a policy for protecting resources using Just-in-Time access control

    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param asc_location: The location where ASC stores the data of the subscription. can be retrieved from Get locations
    :type asc_location: str
    :param jit_network_access_policy_name: Name of a Just-in-Time access configuration policy.
    :type jit_network_access_policy_name: str
    :param api_version: API version for the operation
    :type api_version: str
    :param body: 
    :type body: dict | bytes

    """
    body = JitNetworkAccessPolicy.from_dict(body)
    return web.Response(status=200)


async def jit_network_access_policies_delete(request: web.Request, subscription_id, resource_group_name, asc_location, jit_network_access_policy_name, api_version) -> web.Response:
    """jit_network_access_policies_delete

    Delete a Just-in-Time access control policy.

    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param asc_location: The location where ASC stores the data of the subscription. can be retrieved from Get locations
    :type asc_location: str
    :param jit_network_access_policy_name: Name of a Just-in-Time access configuration policy.
    :type jit_network_access_policy_name: str
    :param api_version: API version for the operation
    :type api_version: str

    """
    return web.Response(status=200)


async def jit_network_access_policies_get(request: web.Request, subscription_id, resource_group_name, asc_location, jit_network_access_policy_name, api_version) -> web.Response:
    """jit_network_access_policies_get

    Policies for protecting resources using Just-in-Time access control for the subscription, location

    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param asc_location: The location where ASC stores the data of the subscription. can be retrieved from Get locations
    :type asc_location: str
    :param jit_network_access_policy_name: Name of a Just-in-Time access configuration policy.
    :type jit_network_access_policy_name: str
    :param api_version: API version for the operation
    :type api_version: str

    """
    return web.Response(status=200)


async def jit_network_access_policies_initiate(request: web.Request, subscription_id, resource_group_name, asc_location, jit_network_access_policy_name, jit_network_access_policy_initiate_type, api_version, body) -> web.Response:
    """jit_network_access_policies_initiate

    Initiate a JIT access from a specific Just-in-Time policy configuration.

    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param asc_location: The location where ASC stores the data of the subscription. can be retrieved from Get locations
    :type asc_location: str
    :param jit_network_access_policy_name: Name of a Just-in-Time access configuration policy.
    :type jit_network_access_policy_name: str
    :param jit_network_access_policy_initiate_type: Type of the action to do on the Just-in-Time access policy.
    :type jit_network_access_policy_initiate_type: str
    :param api_version: API version for the operation
    :type api_version: str
    :param body: 
    :type body: dict | bytes

    """
    body = JitNetworkAccessPolicyInitiateRequest.from_dict(body)
    return web.Response(status=200)


async def jit_network_access_policies_list(request: web.Request, subscription_id, api_version) -> web.Response:
    """jit_network_access_policies_list

    Policies for protecting resources using Just-in-Time access control.

    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param api_version: API version for the operation
    :type api_version: str

    """
    return web.Response(status=200)


async def jit_network_access_policies_list_by_region(request: web.Request, subscription_id, asc_location, api_version) -> web.Response:
    """jit_network_access_policies_list_by_region

    Policies for protecting resources using Just-in-Time access control for the subscription, location

    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param asc_location: The location where ASC stores the data of the subscription. can be retrieved from Get locations
    :type asc_location: str
    :param api_version: API version for the operation
    :type api_version: str

    """
    return web.Response(status=200)


async def jit_network_access_policies_list_by_resource_group(request: web.Request, subscription_id, resource_group_name, api_version) -> web.Response:
    """jit_network_access_policies_list_by_resource_group

    Policies for protecting resources using Just-in-Time access control for the subscription, location

    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: API version for the operation
    :type api_version: str

    """
    return web.Response(status=200)


async def jit_network_access_policies_list_by_resource_group_and_region(request: web.Request, subscription_id, resource_group_name, asc_location, api_version) -> web.Response:
    """jit_network_access_policies_list_by_resource_group_and_region

    Policies for protecting resources using Just-in-Time access control for the subscription, location

    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param asc_location: The location where ASC stores the data of the subscription. can be retrieved from Get locations
    :type asc_location: str
    :param api_version: API version for the operation
    :type api_version: str

    """
    return web.Response(status=200)

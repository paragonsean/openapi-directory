from typing import List, Dict
from aiohttp import web

from openapi_server.models.service_endpoint_policies_update_request import ServiceEndpointPoliciesUpdateRequest
from openapi_server.models.service_endpoint_policy import ServiceEndpointPolicy
from openapi_server.models.service_endpoint_policy_list_result import ServiceEndpointPolicyListResult
from openapi_server import util


async def service_endpoint_policies_create_or_update(request: web.Request, resource_group_name, service_endpoint_policy_name, api_version, subscription_id, parameters) -> web.Response:
    """service_endpoint_policies_create_or_update

    Creates or updates a service Endpoint Policies.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_endpoint_policy_name: The name of the service endpoint policy.
    :type service_endpoint_policy_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the create or update service endpoint policy operation.
    :type parameters: dict | bytes

    """
    parameters = ServiceEndpointPolicy.from_dict(parameters)
    return web.Response(status=200)


async def service_endpoint_policies_delete(request: web.Request, resource_group_name, service_endpoint_policy_name, api_version, subscription_id) -> web.Response:
    """service_endpoint_policies_delete

    Deletes the specified service endpoint policy.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_endpoint_policy_name: The name of the service endpoint policy.
    :type service_endpoint_policy_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def service_endpoint_policies_get(request: web.Request, resource_group_name, service_endpoint_policy_name, api_version, subscription_id, expand=None) -> web.Response:
    """service_endpoint_policies_get

    Gets the specified service Endpoint Policies in a specified resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_endpoint_policy_name: The name of the service endpoint policy.
    :type service_endpoint_policy_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param expand: Expands referenced resources.
    :type expand: str

    """
    return web.Response(status=200)


async def service_endpoint_policies_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """service_endpoint_policies_list

    Gets all the service endpoint policies in a subscription.

    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def service_endpoint_policies_update(request: web.Request, resource_group_name, service_endpoint_policy_name, api_version, subscription_id, parameters) -> web.Response:
    """service_endpoint_policies_update

    Updates service Endpoint Policies.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_endpoint_policy_name: The name of the service endpoint policy.
    :type service_endpoint_policy_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to update service endpoint policy tags.
    :type parameters: dict | bytes

    """
    parameters = ServiceEndpointPoliciesUpdateRequest.from_dict(parameters)
    return web.Response(status=200)

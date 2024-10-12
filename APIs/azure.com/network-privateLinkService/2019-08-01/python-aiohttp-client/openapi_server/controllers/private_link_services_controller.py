from typing import List, Dict
from aiohttp import web

from openapi_server.models.auto_approved_private_link_services_result import AutoApprovedPrivateLinkServicesResult
from openapi_server.models.check_private_link_service_visibility_request import CheckPrivateLinkServiceVisibilityRequest
from openapi_server.models.private_endpoint_connection import PrivateEndpointConnection
from openapi_server.models.private_link_service import PrivateLinkService
from openapi_server.models.private_link_service_list_result import PrivateLinkServiceListResult
from openapi_server.models.private_link_service_visibility import PrivateLinkServiceVisibility
from openapi_server.models.private_link_services_list_by_subscription_default_response import PrivateLinkServicesListBySubscriptionDefaultResponse
from openapi_server import util


async def private_link_services_check_private_link_service_visibility(request: web.Request, location, api_version, subscription_id, parameters) -> web.Response:
    """private_link_services_check_private_link_service_visibility

    Checks whether the subscription is visible to private link service.

    :param location: The location of the domain name.
    :type location: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: The request body of CheckPrivateLinkService API call.
    :type parameters: dict | bytes

    """
    parameters = CheckPrivateLinkServiceVisibilityRequest.from_dict(parameters)
    return web.Response(status=200)


async def private_link_services_check_private_link_service_visibility_by_resource_group(request: web.Request, location, resource_group_name, api_version, subscription_id, parameters) -> web.Response:
    """private_link_services_check_private_link_service_visibility_by_resource_group

    Checks whether the subscription is visible to private link service in the specified resource group.

    :param location: The location of the domain name.
    :type location: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: The request body of CheckPrivateLinkService API call.
    :type parameters: dict | bytes

    """
    parameters = CheckPrivateLinkServiceVisibilityRequest.from_dict(parameters)
    return web.Response(status=200)


async def private_link_services_delete(request: web.Request, resource_group_name, service_name, api_version, subscription_id) -> web.Response:
    """private_link_services_delete

    Deletes the specified private link service.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the private link service.
    :type service_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def private_link_services_delete_private_endpoint_connection(request: web.Request, resource_group_name, service_name, pe_connection_name, api_version, subscription_id) -> web.Response:
    """private_link_services_delete_private_endpoint_connection

    Delete private end point connection for a private link service in a subscription.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the private link service.
    :type service_name: str
    :param pe_connection_name: The name of the private end point connection.
    :type pe_connection_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def private_link_services_get(request: web.Request, resource_group_name, service_name, api_version, subscription_id, expand=None) -> web.Response:
    """private_link_services_get

    Gets the specified private link service by resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the private link service.
    :type service_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param expand: Expands referenced resources.
    :type expand: str

    """
    return web.Response(status=200)


async def private_link_services_list(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """private_link_services_list

    Gets all private link services in a resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def private_link_services_list_auto_approved_private_link_services(request: web.Request, location, api_version, subscription_id) -> web.Response:
    """private_link_services_list_auto_approved_private_link_services

    Returns all of the private link service ids that can be linked to a Private Endpoint with auto approved in this subscription in this region.

    :param location: The location of the domain name.
    :type location: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def private_link_services_list_auto_approved_private_link_services_by_resource_group(request: web.Request, location, resource_group_name, api_version, subscription_id) -> web.Response:
    """private_link_services_list_auto_approved_private_link_services_by_resource_group

    Returns all of the private link service ids that can be linked to a Private Endpoint with auto approved in this subscription in this region.

    :param location: The location of the domain name.
    :type location: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def private_link_services_list_by_subscription(request: web.Request, api_version, subscription_id) -> web.Response:
    """private_link_services_list_by_subscription

    Gets all private link service in a subscription.

    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def private_link_services_update_private_endpoint_connection(request: web.Request, resource_group_name, service_name, pe_connection_name, api_version, subscription_id, parameters) -> web.Response:
    """private_link_services_update_private_endpoint_connection

    Approve or reject private end point connection for a private link service in a subscription.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the private link service.
    :type service_name: str
    :param pe_connection_name: The name of the private end point connection.
    :type pe_connection_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to approve or reject the private end point connection.
    :type parameters: dict | bytes

    """
    parameters = PrivateEndpointConnection.from_dict(parameters)
    return web.Response(status=200)

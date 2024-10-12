from typing import List, Dict
from aiohttp import web

from openapi_server.models.nat_gateway import NatGateway
from openapi_server.models.nat_gateway_list_result import NatGatewayListResult
from openapi_server.models.nat_gateways_update_tags_request import NatGatewaysUpdateTagsRequest
from openapi_server import util


async def nat_gateways_create_or_update(request: web.Request, resource_group_name, nat_gateway_name, api_version, subscription_id, parameters) -> web.Response:
    """nat_gateways_create_or_update

    Creates or updates a nat gateway.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param nat_gateway_name: The name of the nat gateway.
    :type nat_gateway_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the create or update nat gateway operation.
    :type parameters: dict | bytes

    """
    parameters = NatGateway.from_dict(parameters)
    return web.Response(status=200)


async def nat_gateways_delete(request: web.Request, resource_group_name, nat_gateway_name, api_version, subscription_id) -> web.Response:
    """nat_gateways_delete

    Deletes the specified nat gateway.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param nat_gateway_name: The name of the nat gateway.
    :type nat_gateway_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def nat_gateways_get(request: web.Request, resource_group_name, nat_gateway_name, api_version, subscription_id, expand=None) -> web.Response:
    """nat_gateways_get

    Gets the specified nat gateway in a specified resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param nat_gateway_name: The name of the nat gateway.
    :type nat_gateway_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param expand: Expands referenced resources.
    :type expand: str

    """
    return web.Response(status=200)


async def nat_gateways_list(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """nat_gateways_list

    Gets all nat gateways in a resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def nat_gateways_list_all(request: web.Request, api_version, subscription_id) -> web.Response:
    """nat_gateways_list_all

    Gets all the Nat Gateways in a subscription.

    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def nat_gateways_update_tags(request: web.Request, resource_group_name, nat_gateway_name, api_version, subscription_id, parameters) -> web.Response:
    """nat_gateways_update_tags

    Updates nat gateway tags.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param nat_gateway_name: The name of the nat gateway.
    :type nat_gateway_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to update nat gateway tags.
    :type parameters: dict | bytes

    """
    parameters = NatGatewaysUpdateTagsRequest.from_dict(parameters)
    return web.Response(status=200)

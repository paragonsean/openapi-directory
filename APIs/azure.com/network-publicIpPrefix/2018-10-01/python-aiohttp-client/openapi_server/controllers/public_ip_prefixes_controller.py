from typing import List, Dict
from aiohttp import web

from openapi_server.models.public_ip_prefix import PublicIPPrefix
from openapi_server.models.public_ip_prefix_list_result import PublicIPPrefixListResult
from openapi_server.models.public_ip_prefixes_update_tags_request import PublicIPPrefixesUpdateTagsRequest
from openapi_server import util


async def public_ip_prefixes_create_or_update(request: web.Request, resource_group_name, public_ip_prefix_name, api_version, subscription_id, parameters) -> web.Response:
    """public_ip_prefixes_create_or_update

    Creates or updates a static or dynamic public IP prefix.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param public_ip_prefix_name: The name of the public IP prefix.
    :type public_ip_prefix_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the create or update public IP prefix operation.
    :type parameters: dict | bytes

    """
    parameters = PublicIPPrefix.from_dict(parameters)
    return web.Response(status=200)


async def public_ip_prefixes_delete(request: web.Request, resource_group_name, public_ip_prefix_name, api_version, subscription_id) -> web.Response:
    """public_ip_prefixes_delete

    Deletes the specified public IP prefix.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param public_ip_prefix_name: The name of the PublicIpPrefix.
    :type public_ip_prefix_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def public_ip_prefixes_get(request: web.Request, resource_group_name, public_ip_prefix_name, api_version, subscription_id, expand=None) -> web.Response:
    """public_ip_prefixes_get

    Gets the specified public IP prefix in a specified resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param public_ip_prefix_name: The name of the Public IP Prefix.
    :type public_ip_prefix_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param expand: Expands referenced resources.
    :type expand: str

    """
    return web.Response(status=200)


async def public_ip_prefixes_list(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """public_ip_prefixes_list

    Gets all public IP prefixes in a resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def public_ip_prefixes_list_all(request: web.Request, api_version, subscription_id) -> web.Response:
    """public_ip_prefixes_list_all

    Gets all the public IP prefixes in a subscription.

    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def public_ip_prefixes_update_tags(request: web.Request, resource_group_name, public_ip_prefix_name, api_version, subscription_id, parameters) -> web.Response:
    """public_ip_prefixes_update_tags

    Updates public IP prefix tags.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param public_ip_prefix_name: The name of the public IP prefix.
    :type public_ip_prefix_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to update public IP prefix tags.
    :type parameters: dict | bytes

    """
    parameters = PublicIPPrefixesUpdateTagsRequest.from_dict(parameters)
    return web.Response(status=200)

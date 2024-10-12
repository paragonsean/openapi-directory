from typing import List, Dict
from aiohttp import web

from openapi_server.models.azure_firewall import AzureFirewall
from openapi_server.models.azure_firewall_list_result import AzureFirewallListResult
from openapi_server import util


async def azure_firewalls_create_or_update(request: web.Request, resource_group_name, azure_firewall_name, api_version, subscription_id, parameters) -> web.Response:
    """azure_firewalls_create_or_update

    Creates or updates the specified Azure Firewall.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param azure_firewall_name: The name of the Azure Firewall.
    :type azure_firewall_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the create or update Azure Firewall operation.
    :type parameters: dict | bytes

    """
    parameters = AzureFirewall.from_dict(parameters)
    return web.Response(status=200)


async def azure_firewalls_delete(request: web.Request, resource_group_name, azure_firewall_name, api_version, subscription_id) -> web.Response:
    """azure_firewalls_delete

    Deletes the specified Azure Firewall.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param azure_firewall_name: The name of the Azure Firewall.
    :type azure_firewall_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def azure_firewalls_get(request: web.Request, resource_group_name, azure_firewall_name, api_version, subscription_id) -> web.Response:
    """azure_firewalls_get

    Gets the specified Azure Firewall.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param azure_firewall_name: The name of the Azure Firewall.
    :type azure_firewall_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def azure_firewalls_list(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """azure_firewalls_list

    Lists all Azure Firewalls in a resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def azure_firewalls_list_all(request: web.Request, api_version, subscription_id) -> web.Response:
    """azure_firewalls_list_all

    Gets all the Azure Firewalls in a subscription.

    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def azure_firewalls_update_tags(request: web.Request, resource_group_name, azure_firewall_name, api_version, subscription_id, parameters) -> web.Response:
    """azure_firewalls_update_tags

    Updates tags for an Azure Firewall resource.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param azure_firewall_name: The name of the Azure Firewall.
    :type azure_firewall_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the create or update Azure Firewall operation.
    :type parameters: dict | bytes

    """
    parameters = AzureFirewall.from_dict(parameters)
    return web.Response(status=200)

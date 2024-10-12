from typing import List, Dict
from aiohttp import web

from openapi_server.models.bastion_host import BastionHost
from openapi_server.models.bastion_host_list_result import BastionHostListResult
from openapi_server import util


async def bastion_hosts_create_or_update(request: web.Request, resource_group_name, bastion_host_name, api_version, subscription_id, parameters) -> web.Response:
    """bastion_hosts_create_or_update

    Creates or updates the specified Bastion Host.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param bastion_host_name: The name of the Bastion Host.
    :type bastion_host_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the create or update Bastion Host operation.
    :type parameters: dict | bytes

    """
    parameters = BastionHost.from_dict(parameters)
    return web.Response(status=200)


async def bastion_hosts_delete(request: web.Request, resource_group_name, bastion_host_name, api_version, subscription_id) -> web.Response:
    """bastion_hosts_delete

    Deletes the specified Bastion Host.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param bastion_host_name: The name of the Bastion Host.
    :type bastion_host_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def bastion_hosts_get(request: web.Request, resource_group_name, bastion_host_name, api_version, subscription_id) -> web.Response:
    """bastion_hosts_get

    Gets the specified Bastion Host.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param bastion_host_name: The name of the Bastion Host.
    :type bastion_host_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def bastion_hosts_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """bastion_hosts_list

    Lists all Bastion Hosts in a subscription.

    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def bastion_hosts_list_by_resource_group(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """bastion_hosts_list_by_resource_group

    Lists all Bastion Hosts in a resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)

from typing import List, Dict
from aiohttp import web

from openapi_server.models.server_dns_alias import ServerDnsAlias
from openapi_server.models.server_dns_alias_acquisition import ServerDnsAliasAcquisition
from openapi_server.models.server_dns_alias_list_result import ServerDnsAliasListResult
from openapi_server import util


async def server_dns_aliases_acquire(request: web.Request, resource_group_name, server_name, dns_alias_name, subscription_id, api_version, parameters) -> web.Response:
    """server_dns_aliases_acquire

    Acquires server DNS alias from another server.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server that the alias is pointing to.
    :type server_name: str
    :param dns_alias_name: The name of the server dns alias.
    :type dns_alias_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str
    :param parameters: 
    :type parameters: dict | bytes

    """
    parameters = ServerDnsAliasAcquisition.from_dict(parameters)
    return web.Response(status=200)


async def server_dns_aliases_create_or_update(request: web.Request, resource_group_name, server_name, dns_alias_name, subscription_id, api_version) -> web.Response:
    """server_dns_aliases_create_or_update

    Creates a server dns alias.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server that the alias is pointing to.
    :type server_name: str
    :param dns_alias_name: The name of the server DNS alias.
    :type dns_alias_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def server_dns_aliases_delete(request: web.Request, resource_group_name, server_name, dns_alias_name, subscription_id, api_version) -> web.Response:
    """server_dns_aliases_delete

    Deletes the server DNS alias with the given name.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server that the alias is pointing to.
    :type server_name: str
    :param dns_alias_name: The name of the server DNS alias.
    :type dns_alias_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def server_dns_aliases_get(request: web.Request, resource_group_name, server_name, dns_alias_name, subscription_id, api_version) -> web.Response:
    """server_dns_aliases_get

    Gets a server DNS alias.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server that the alias is pointing to.
    :type server_name: str
    :param dns_alias_name: The name of the server DNS alias.
    :type dns_alias_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def server_dns_aliases_list_by_server(request: web.Request, resource_group_name, server_name, subscription_id, api_version) -> web.Response:
    """server_dns_aliases_list_by_server

    Gets a list of server DNS aliases for a server.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server that the alias is pointing to.
    :type server_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)

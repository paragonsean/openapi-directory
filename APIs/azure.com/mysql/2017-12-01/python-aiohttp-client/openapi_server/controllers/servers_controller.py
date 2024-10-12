from typing import List, Dict
from aiohttp import web

from openapi_server.models.server import Server
from openapi_server.models.server_for_create import ServerForCreate
from openapi_server.models.server_list_result import ServerListResult
from openapi_server.models.server_update_parameters import ServerUpdateParameters
from openapi_server import util


async def servers_create(request: web.Request, api_version, subscription_id, resource_group_name, server_name, parameters) -> web.Response:
    """servers_create

    Creates a new server or updates an existing server. The update action will overwrite the existing server.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param parameters: The required parameters for creating or updating a server.
    :type parameters: dict | bytes

    """
    parameters = ServerForCreate.from_dict(parameters)
    return web.Response(status=200)


async def servers_delete(request: web.Request, api_version, subscription_id, resource_group_name, server_name) -> web.Response:
    """servers_delete

    Deletes a server.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str

    """
    return web.Response(status=200)


async def servers_get(request: web.Request, api_version, subscription_id, resource_group_name, server_name) -> web.Response:
    """servers_get

    Gets information about a server.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str

    """
    return web.Response(status=200)


async def servers_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """servers_list

    List all the servers in a given subscription.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def servers_list_by_resource_group(request: web.Request, api_version, subscription_id, resource_group_name) -> web.Response:
    """servers_list_by_resource_group

    List all the servers in a given resource group.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str

    """
    return web.Response(status=200)


async def servers_update(request: web.Request, api_version, subscription_id, resource_group_name, server_name, parameters) -> web.Response:
    """servers_update

    Updates an existing server. The request body can contain one to many of the properties present in the normal server definition.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param parameters: The required parameters for updating a server.
    :type parameters: dict | bytes

    """
    parameters = ServerUpdateParameters.from_dict(parameters)
    return web.Response(status=200)

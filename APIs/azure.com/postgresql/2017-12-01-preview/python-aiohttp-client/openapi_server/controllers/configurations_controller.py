from typing import List, Dict
from aiohttp import web

from openapi_server.models.configuration import Configuration
from openapi_server.models.configuration_list_result import ConfigurationListResult
from openapi_server import util


async def configurations_create_or_update(request: web.Request, api_version, subscription_id, resource_group_name, server_name, configuration_name, parameters) -> web.Response:
    """configurations_create_or_update

    Updates a configuration of a server.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param configuration_name: The name of the server configuration.
    :type configuration_name: str
    :param parameters: The required parameters for updating a server configuration.
    :type parameters: dict | bytes

    """
    parameters = Configuration.from_dict(parameters)
    return web.Response(status=200)


async def configurations_get(request: web.Request, api_version, subscription_id, resource_group_name, server_name, configuration_name) -> web.Response:
    """configurations_get

    Gets information about a configuration of server.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param configuration_name: The name of the server configuration.
    :type configuration_name: str

    """
    return web.Response(status=200)


async def configurations_list_by_server(request: web.Request, api_version, subscription_id, resource_group_name, server_name) -> web.Response:
    """configurations_list_by_server

    List all the configurations in a given server.

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

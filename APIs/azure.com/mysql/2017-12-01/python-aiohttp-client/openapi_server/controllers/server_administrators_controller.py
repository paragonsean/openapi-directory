from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.server_administrator_resource import ServerAdministratorResource
from openapi_server.models.server_administrator_resource_list_result import ServerAdministratorResourceListResult
from openapi_server import util


async def server_administrators_create_or_update(request: web.Request, api_version, subscription_id, resource_group_name, server_name, properties) -> web.Response:
    """server_administrators_create_or_update

    Creates or update active directory administrator on an existing server. The update action will overwrite the existing administrator.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param properties: The required parameters for creating or updating an AAD server administrator.
    :type properties: dict | bytes

    """
    properties = ServerAdministratorResource.from_dict(properties)
    return web.Response(status=200)


async def server_administrators_delete(request: web.Request, api_version, subscription_id, resource_group_name, server_name) -> web.Response:
    """server_administrators_delete

    Deletes AAD Administrator.

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


async def server_administrators_get(request: web.Request, api_version, subscription_id, resource_group_name, server_name) -> web.Response:
    """server_administrators_get

    Gets information about a AAD server administrator.

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


async def server_administrators_list_by_server(request: web.Request, api_version, subscription_id, resource_group_name, server_name) -> web.Response:
    """server_administrators_list_by_server

    Returns a list of server Administrators.

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

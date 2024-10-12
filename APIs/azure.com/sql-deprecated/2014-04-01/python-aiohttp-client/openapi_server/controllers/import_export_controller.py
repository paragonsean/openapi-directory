from typing import List, Dict
from aiohttp import web

from openapi_server.models.extension_list_result import ExtensionListResult
from openapi_server import util


async def extensions_get(request: web.Request, api_version, subscription_id, resource_group_name, server_name, database_name, extension_name) -> web.Response:
    """extensions_get

    Gets a database extension. This API is deprecated and should not be used.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database to import into
    :type database_name: str
    :param extension_name: The name of the extension to get
    :type extension_name: str

    """
    return web.Response(status=200)


async def extensions_list_by_database(request: web.Request, api_version, subscription_id, resource_group_name, server_name, database_name) -> web.Response:
    """extensions_list_by_database

    Gets database extensions. This API is deprecated and should not be used.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database to import into
    :type database_name: str

    """
    return web.Response(status=200)

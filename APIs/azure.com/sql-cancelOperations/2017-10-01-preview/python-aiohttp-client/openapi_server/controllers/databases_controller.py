from typing import List, Dict
from aiohttp import web

from openapi_server.models.database_operation_list_result import DatabaseOperationListResult
from openapi_server import util


async def database_operations_cancel(request: web.Request, resource_group_name, server_name, database_name, operation_id, subscription_id, api_version) -> web.Response:
    """database_operations_cancel

    Cancels the asynchronous operation on the database.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database.
    :type database_name: str
    :param operation_id: The operation identifier.
    :type operation_id: str
    :type operation_id: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def database_operations_list_by_database(request: web.Request, resource_group_name, server_name, database_name, subscription_id, api_version) -> web.Response:
    """database_operations_list_by_database

    Gets a list of operations performed on the database.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database.
    :type database_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)

from typing import List, Dict
from aiohttp import web

from openapi_server.models.recoverable_managed_database import RecoverableManagedDatabase
from openapi_server.models.recoverable_managed_database_list_result import RecoverableManagedDatabaseListResult
from openapi_server import util


async def recoverable_managed_databases_get(request: web.Request, resource_group_name, managed_instance_name, recoverable_database_name, subscription_id, api_version) -> web.Response:
    """recoverable_managed_databases_get

    Gets a recoverable managed database.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param managed_instance_name: The name of the managed instance.
    :type managed_instance_name: str
    :param recoverable_database_name: 
    :type recoverable_database_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def recoverable_managed_databases_list_by_instance(request: web.Request, resource_group_name, managed_instance_name, subscription_id, api_version) -> web.Response:
    """recoverable_managed_databases_list_by_instance

    Gets a list of recoverable managed databases.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param managed_instance_name: The name of the managed instance.
    :type managed_instance_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)

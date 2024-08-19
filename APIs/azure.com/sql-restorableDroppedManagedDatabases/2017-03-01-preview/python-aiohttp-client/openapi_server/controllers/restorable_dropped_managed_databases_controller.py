from typing import List, Dict
from aiohttp import web

from openapi_server.models.restorable_dropped_managed_database import RestorableDroppedManagedDatabase
from openapi_server.models.restorable_dropped_managed_database_list_result import RestorableDroppedManagedDatabaseListResult
from openapi_server import util


async def restorable_dropped_managed_databases_get(request: web.Request, resource_group_name, managed_instance_name, restorable_dropped_database_id, subscription_id, api_version) -> web.Response:
    """restorable_dropped_managed_databases_get

    Gets a restorable dropped managed database.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param managed_instance_name: The name of the managed instance.
    :type managed_instance_name: str
    :param restorable_dropped_database_id: 
    :type restorable_dropped_database_id: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def restorable_dropped_managed_databases_list_by_instance(request: web.Request, resource_group_name, managed_instance_name, subscription_id, api_version) -> web.Response:
    """restorable_dropped_managed_databases_list_by_instance

    Gets a list of restorable dropped managed databases.

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

from typing import List, Dict
from aiohttp import web

from openapi_server.models.workload_group import WorkloadGroup
from openapi_server.models.workload_group_list_result import WorkloadGroupListResult
from openapi_server import util


async def workload_groups_create_or_update(request: web.Request, resource_group_name, server_name, database_name, workload_group_name, subscription_id, api_version, parameters) -> web.Response:
    """workload_groups_create_or_update

    Creates or updates a workload group.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database.
    :type database_name: str
    :param workload_group_name: The name of the workload group.
    :type workload_group_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str
    :param parameters: The requested workload group state.
    :type parameters: dict | bytes

    """
    parameters = WorkloadGroup.from_dict(parameters)
    return web.Response(status=200)


async def workload_groups_delete(request: web.Request, resource_group_name, server_name, database_name, workload_group_name, subscription_id, api_version) -> web.Response:
    """workload_groups_delete

    Deletes a workload group.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database.
    :type database_name: str
    :param workload_group_name: The name of the workload group to delete.
    :type workload_group_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def workload_groups_get(request: web.Request, resource_group_name, server_name, database_name, workload_group_name, subscription_id, api_version) -> web.Response:
    """workload_groups_get

    Gets a workload group

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database.
    :type database_name: str
    :param workload_group_name: The name of the workload group.
    :type workload_group_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def workload_groups_list_by_database(request: web.Request, resource_group_name, server_name, database_name, subscription_id, api_version) -> web.Response:
    """workload_groups_list_by_database

    Gets the list of workload groups

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

from typing import List, Dict
from aiohttp import web

from openapi_server.models.managed_instance_administrator import ManagedInstanceAdministrator
from openapi_server.models.managed_instance_administrator_list_result import ManagedInstanceAdministratorListResult
from openapi_server import util


async def managed_instance_administrators_create_or_update(request: web.Request, resource_group_name, managed_instance_name, administrator_name, subscription_id, api_version, parameters) -> web.Response:
    """managed_instance_administrators_create_or_update

    Creates or updates a managed instance administrator.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param managed_instance_name: The name of the managed instance.
    :type managed_instance_name: str
    :param administrator_name: The requested administrator name.
    :type administrator_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str
    :param parameters: The requested administrator parameters.
    :type parameters: dict | bytes

    """
    parameters = ManagedInstanceAdministrator.from_dict(parameters)
    return web.Response(status=200)


async def managed_instance_administrators_delete(request: web.Request, resource_group_name, managed_instance_name, administrator_name, subscription_id, api_version) -> web.Response:
    """managed_instance_administrators_delete

    Deletes a managed instance administrator.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param managed_instance_name: The name of the managed instance.
    :type managed_instance_name: str
    :param administrator_name: The administrator name.
    :type administrator_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def managed_instance_administrators_get(request: web.Request, resource_group_name, managed_instance_name, administrator_name, subscription_id, api_version) -> web.Response:
    """managed_instance_administrators_get

    Gets a managed instance administrator.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param managed_instance_name: The name of the managed instance.
    :type managed_instance_name: str
    :param administrator_name: The administrator name.
    :type administrator_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def managed_instance_administrators_list_by_instance(request: web.Request, resource_group_name, managed_instance_name, subscription_id, api_version) -> web.Response:
    """managed_instance_administrators_list_by_instance

    Gets a list of managed instance administrators.

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

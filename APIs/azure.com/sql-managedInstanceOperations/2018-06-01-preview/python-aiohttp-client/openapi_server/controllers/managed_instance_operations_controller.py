from typing import List, Dict
from aiohttp import web

from openapi_server.models.managed_instance_operation_list_result import ManagedInstanceOperationListResult
from openapi_server import util


async def managed_instance_operations_list_by_managed_instance(request: web.Request, resource_group_name, managed_instance_name, subscription_id, api_version) -> web.Response:
    """managed_instance_operations_list_by_managed_instance

    Gets a list of operations performed on the managed instance.

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

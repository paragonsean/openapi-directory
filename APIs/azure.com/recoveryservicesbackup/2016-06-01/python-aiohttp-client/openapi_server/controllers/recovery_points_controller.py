from typing import List, Dict
from aiohttp import web

from openapi_server.models.recovery_point_resource import RecoveryPointResource
from openapi_server.models.recovery_point_resource_list import RecoveryPointResourceList
from openapi_server import util


async def recovery_points_get(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, fabric_name, container_name, protected_item_name, recovery_point_id) -> web.Response:
    """recovery_points_get

    Provides the backup data for the RecoveryPointID. This is an asynchronous operation. To learn the status of the operation, call the GetProtectedItemOperationResult API.

    :param api_version: Client API version.
    :type api_version: str
    :param vault_name: The name of the Recovery Services vault.
    :type vault_name: str
    :param resource_group_name: The name of the resource group associated with the Recovery Services vault.
    :type resource_group_name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param fabric_name: The fabric name associated with backup item.
    :type fabric_name: str
    :param container_name: The container name associated with backup item.
    :type container_name: str
    :param protected_item_name: The name of the backup item used in this GET operation.
    :type protected_item_name: str
    :param recovery_point_id: The RecoveryPointID associated with this GET operation.
    :type recovery_point_id: str

    """
    return web.Response(status=200)


async def recovery_points_list(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, fabric_name, container_name, protected_item_name, filter=None) -> web.Response:
    """recovery_points_list

    Lists the recovery points, or backup copies, for the specified backup item.

    :param api_version: Client API version.
    :type api_version: str
    :param vault_name: The name of the Recovery Services vault.
    :type vault_name: str
    :param resource_group_name: The name of the resource group associated with the Recovery Services vault.
    :type resource_group_name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param fabric_name: The fabric name associated with the backup item.
    :type fabric_name: str
    :param container_name: The container name associated with the backup item.
    :type container_name: str
    :param protected_item_name: The name of backup item used in this GET operation.
    :type protected_item_name: str
    :param filter: startDate eq {yyyy-mm-dd hh:mm:ss PM} and endDate { yyyy-mm-dd hh:mm:ss PM}.
    :type filter: str

    """
    return web.Response(status=200)

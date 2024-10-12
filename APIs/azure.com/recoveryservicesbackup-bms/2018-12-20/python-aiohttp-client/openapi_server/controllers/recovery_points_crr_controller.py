from typing import List, Dict
from aiohttp import web

from openapi_server.models.recovery_point_resource_list import RecoveryPointResourceList
from openapi_server import util


async def recovery_points_crr_list(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, fabric_name, container_name, protected_item_name, filter=None) -> web.Response:
    """recovery_points_crr_list

    Lists the backup copies for the backed up item.

    :param api_version: Client Api Version.
    :type api_version: str
    :param vault_name: The name of the recovery services vault.
    :type vault_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: Fabric name associated with the backed up item.
    :type fabric_name: str
    :param container_name: Container name associated with the backed up item.
    :type container_name: str
    :param protected_item_name: Backed up item whose backup copies are to be fetched.
    :type protected_item_name: str
    :param filter: OData filter options.
    :type filter: str

    """
    return web.Response(status=200)

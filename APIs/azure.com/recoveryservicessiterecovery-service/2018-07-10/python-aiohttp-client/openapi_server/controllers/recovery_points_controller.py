from typing import List, Dict
from aiohttp import web

from openapi_server.models.recovery_point import RecoveryPoint
from openapi_server.models.recovery_point_collection import RecoveryPointCollection
from openapi_server import util


async def recovery_points_get(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, protection_container_name, replicated_protected_item_name, recovery_point_name) -> web.Response:
    """Get a recovery point.

    Get the details of specified recovery point.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: The fabric name.
    :type fabric_name: str
    :param protection_container_name: The protection container name.
    :type protection_container_name: str
    :param replicated_protected_item_name: The replication protected item&#39;s name.
    :type replicated_protected_item_name: str
    :param recovery_point_name: The recovery point name.
    :type recovery_point_name: str

    """
    return web.Response(status=200)


async def recovery_points_list_by_replication_protected_items(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, protection_container_name, replicated_protected_item_name) -> web.Response:
    """Get recovery points for a replication protected item.

    Lists the available recovery points for a replication protected item.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: The fabric name.
    :type fabric_name: str
    :param protection_container_name: The protection container name.
    :type protection_container_name: str
    :param replicated_protected_item_name: The replication protected item&#39;s name.
    :type replicated_protected_item_name: str

    """
    return web.Response(status=200)

from typing import List, Dict
from aiohttp import web

from openapi_server.models.migration_recovery_point import MigrationRecoveryPoint
from openapi_server.models.migration_recovery_point_collection import MigrationRecoveryPointCollection
from openapi_server import util


async def migration_recovery_points_get(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, protection_container_name, migration_item_name, migration_recovery_point_name) -> web.Response:
    """Gets a recovery point for a migration item.

    

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: Fabric unique name.
    :type fabric_name: str
    :param protection_container_name: Protection container name.
    :type protection_container_name: str
    :param migration_item_name: Migration item name.
    :type migration_item_name: str
    :param migration_recovery_point_name: The migration recovery point name.
    :type migration_recovery_point_name: str

    """
    return web.Response(status=200)


async def migration_recovery_points_list_by_replication_migration_items(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, protection_container_name, migration_item_name) -> web.Response:
    """Gets the recovery points for a migration item.

    

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: Fabric unique name.
    :type fabric_name: str
    :param protection_container_name: Protection container name.
    :type protection_container_name: str
    :param migration_item_name: Migration item name.
    :type migration_item_name: str

    """
    return web.Response(status=200)

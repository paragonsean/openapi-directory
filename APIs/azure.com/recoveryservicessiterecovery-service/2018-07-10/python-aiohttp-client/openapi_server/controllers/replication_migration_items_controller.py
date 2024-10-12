from typing import List, Dict
from aiohttp import web

from openapi_server.models.enable_migration_input import EnableMigrationInput
from openapi_server.models.migrate_input import MigrateInput
from openapi_server.models.migration_item import MigrationItem
from openapi_server.models.migration_item_collection import MigrationItemCollection
from openapi_server.models.test_migrate_cleanup_input import TestMigrateCleanupInput
from openapi_server.models.test_migrate_input import TestMigrateInput
from openapi_server.models.update_migration_item_input import UpdateMigrationItemInput
from openapi_server import util


async def replication_migration_items_create(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, protection_container_name, migration_item_name, input) -> web.Response:
    """Enables migration.

    The operation to create an ASR migration item (enable migration).

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: Fabric name.
    :type fabric_name: str
    :param protection_container_name: Protection container name.
    :type protection_container_name: str
    :param migration_item_name: Migration item name.
    :type migration_item_name: str
    :param input: Enable migration input.
    :type input: dict | bytes

    """
    input = EnableMigrationInput.from_dict(input)
    return web.Response(status=200)


async def replication_migration_items_delete(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, protection_container_name, migration_item_name, delete_option=None) -> web.Response:
    """Delete the migration item.

    The operation to delete an ASR migration item.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: Fabric name.
    :type fabric_name: str
    :param protection_container_name: Protection container name.
    :type protection_container_name: str
    :param migration_item_name: Migration item name.
    :type migration_item_name: str
    :param delete_option: The delete option.
    :type delete_option: str

    """
    return web.Response(status=200)


async def replication_migration_items_get(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, protection_container_name, migration_item_name) -> web.Response:
    """Gets the details of a migration item.

    

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


async def replication_migration_items_list(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, skip_token=None, filter=None) -> web.Response:
    """Gets the list of migration items in the vault.

    

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param skip_token: The pagination token.
    :type skip_token: str
    :param filter: OData filter options.
    :type filter: str

    """
    return web.Response(status=200)


async def replication_migration_items_list_by_replication_protection_containers(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, protection_container_name) -> web.Response:
    """Gets the list of migration items in the protection container.

    Gets the list of ASR migration items in the protection container.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: Fabric name.
    :type fabric_name: str
    :param protection_container_name: Protection container name.
    :type protection_container_name: str

    """
    return web.Response(status=200)


async def replication_migration_items_migrate(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, protection_container_name, migration_item_name, migrate_input) -> web.Response:
    """Migrate item.

    The operation to initiate migration of the item.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: Fabric name.
    :type fabric_name: str
    :param protection_container_name: Protection container name.
    :type protection_container_name: str
    :param migration_item_name: Migration item name.
    :type migration_item_name: str
    :param migrate_input: Migrate input.
    :type migrate_input: dict | bytes

    """
    migrate_input = MigrateInput.from_dict(migrate_input)
    return web.Response(status=200)


async def replication_migration_items_test_migrate(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, protection_container_name, migration_item_name, test_migrate_input) -> web.Response:
    """Test migrate item.

    The operation to initiate test migration of the item.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: Fabric name.
    :type fabric_name: str
    :param protection_container_name: Protection container name.
    :type protection_container_name: str
    :param migration_item_name: Migration item name.
    :type migration_item_name: str
    :param test_migrate_input: Test migrate input.
    :type test_migrate_input: dict | bytes

    """
    test_migrate_input = TestMigrateInput.from_dict(test_migrate_input)
    return web.Response(status=200)


async def replication_migration_items_test_migrate_cleanup(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, protection_container_name, migration_item_name, test_migrate_cleanup_input) -> web.Response:
    """Test migrate cleanup.

    The operation to initiate test migrate cleanup.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: Fabric name.
    :type fabric_name: str
    :param protection_container_name: Protection container name.
    :type protection_container_name: str
    :param migration_item_name: Migration item name.
    :type migration_item_name: str
    :param test_migrate_cleanup_input: Test migrate cleanup input.
    :type test_migrate_cleanup_input: dict | bytes

    """
    test_migrate_cleanup_input = TestMigrateCleanupInput.from_dict(test_migrate_cleanup_input)
    return web.Response(status=200)


async def replication_migration_items_update(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, protection_container_name, migration_item_name, input) -> web.Response:
    """Updates migration item.

    The operation to update the recovery settings of an ASR migration item.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: Fabric name.
    :type fabric_name: str
    :param protection_container_name: Protection container name.
    :type protection_container_name: str
    :param migration_item_name: Migration item name.
    :type migration_item_name: str
    :param input: Update migration item input.
    :type input: dict | bytes

    """
    input = UpdateMigrationItemInput.from_dict(input)
    return web.Response(status=200)

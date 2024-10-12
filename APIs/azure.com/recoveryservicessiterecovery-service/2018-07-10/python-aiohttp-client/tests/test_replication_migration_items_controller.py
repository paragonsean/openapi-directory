# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.enable_migration_input import EnableMigrationInput
from openapi_server.models.migrate_input import MigrateInput
from openapi_server.models.migration_item import MigrationItem
from openapi_server.models.migration_item_collection import MigrationItemCollection
from openapi_server.models.test_migrate_cleanup_input import TestMigrateCleanupInput
from openapi_server.models.test_migrate_input import TestMigrateInput
from openapi_server.models.update_migration_item_input import UpdateMigrationItemInput


pytestmark = pytest.mark.asyncio

async def test_replication_migration_items_create(client):
    """Test case for replication_migration_items_create

    Enables migration.
    """
    input = {"properties":{"policyId":"policyId","providerSpecificDetails":{"instanceType":"instanceType"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationFabrics/{fabric_name}/replicationProtectionContainers/{protection_container_name}/replicationMigrationItems/{migration_item_name}'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', fabric_name='fabric_name_example', protection_container_name='protection_container_name_example', migration_item_name='migration_item_name_example'),
        headers=headers,
        json=input,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replication_migration_items_delete(client):
    """Test case for replication_migration_items_delete

    Delete the migration item.
    """
    params = [('api-version', 'api_version_example'),
                    ('deleteOption', 'delete_option_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationFabrics/{fabric_name}/replicationProtectionContainers/{protection_container_name}/replicationMigrationItems/{migration_item_name}'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', fabric_name='fabric_name_example', protection_container_name='protection_container_name_example', migration_item_name='migration_item_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replication_migration_items_get(client):
    """Test case for replication_migration_items_get

    Gets the details of a migration item.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationFabrics/{fabric_name}/replicationProtectionContainers/{protection_container_name}/replicationMigrationItems/{migration_item_name}'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', fabric_name='fabric_name_example', protection_container_name='protection_container_name_example', migration_item_name='migration_item_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replication_migration_items_list(client):
    """Test case for replication_migration_items_list

    Gets the list of migration items in the vault.
    """
    params = [('api-version', 'api_version_example'),
                    ('skipToken', 'skip_token_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationMigrationItems'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replication_migration_items_list_by_replication_protection_containers(client):
    """Test case for replication_migration_items_list_by_replication_protection_containers

    Gets the list of migration items in the protection container.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationFabrics/{fabric_name}/replicationProtectionContainers/{protection_container_name}/replicationMigrationItems'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', fabric_name='fabric_name_example', protection_container_name='protection_container_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replication_migration_items_migrate(client):
    """Test case for replication_migration_items_migrate

    Migrate item.
    """
    migrate_input = {"properties":{"providerSpecificDetails":{"instanceType":"instanceType"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationFabrics/{fabric_name}/replicationProtectionContainers/{protection_container_name}/replicationMigrationItems/{migration_item_name}/migrate'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', fabric_name='fabric_name_example', protection_container_name='protection_container_name_example', migration_item_name='migration_item_name_example'),
        headers=headers,
        json=migrate_input,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replication_migration_items_test_migrate(client):
    """Test case for replication_migration_items_test_migrate

    Test migrate item.
    """
    test_migrate_input = {"properties":{"providerSpecificDetails":{"instanceType":"instanceType"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationFabrics/{fabric_name}/replicationProtectionContainers/{protection_container_name}/replicationMigrationItems/{migration_item_name}/testMigrate'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', fabric_name='fabric_name_example', protection_container_name='protection_container_name_example', migration_item_name='migration_item_name_example'),
        headers=headers,
        json=test_migrate_input,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replication_migration_items_test_migrate_cleanup(client):
    """Test case for replication_migration_items_test_migrate_cleanup

    Test migrate cleanup.
    """
    test_migrate_cleanup_input = {"properties":{"comments":"comments"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationFabrics/{fabric_name}/replicationProtectionContainers/{protection_container_name}/replicationMigrationItems/{migration_item_name}/testMigrateCleanup'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', fabric_name='fabric_name_example', protection_container_name='protection_container_name_example', migration_item_name='migration_item_name_example'),
        headers=headers,
        json=test_migrate_cleanup_input,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replication_migration_items_update(client):
    """Test case for replication_migration_items_update

    Updates migration item.
    """
    input = {"properties":{"providerSpecificDetails":{"instanceType":"instanceType"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationFabrics/{fabric_name}/replicationProtectionContainers/{protection_container_name}/replicationMigrationItems/{migration_item_name}'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', fabric_name='fabric_name_example', protection_container_name='protection_container_name_example', migration_item_name='migration_item_name_example'),
        headers=headers,
        json=input,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


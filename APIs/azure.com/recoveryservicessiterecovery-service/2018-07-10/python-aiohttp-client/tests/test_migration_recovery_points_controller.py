# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.migration_recovery_point import MigrationRecoveryPoint
from openapi_server.models.migration_recovery_point_collection import MigrationRecoveryPointCollection


pytestmark = pytest.mark.asyncio

async def test_migration_recovery_points_get(client):
    """Test case for migration_recovery_points_get

    Gets a recovery point for a migration item.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationFabrics/{fabric_name}/replicationProtectionContainers/{protection_container_name}/replicationMigrationItems/{migration_item_name}/migrationRecoveryPoints/{migration_recovery_point_name}'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', fabric_name='fabric_name_example', protection_container_name='protection_container_name_example', migration_item_name='migration_item_name_example', migration_recovery_point_name='migration_recovery_point_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_migration_recovery_points_list_by_replication_migration_items(client):
    """Test case for migration_recovery_points_list_by_replication_migration_items

    Gets the recovery points for a migration item.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationFabrics/{fabric_name}/replicationProtectionContainers/{protection_container_name}/replicationMigrationItems/{migration_item_name}/migrationRecoveryPoints'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', fabric_name='fabric_name_example', protection_container_name='protection_container_name_example', migration_item_name='migration_item_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


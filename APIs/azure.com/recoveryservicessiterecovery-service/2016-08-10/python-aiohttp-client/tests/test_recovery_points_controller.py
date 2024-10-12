# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.recovery_point import RecoveryPoint
from openapi_server.models.recovery_point_collection import RecoveryPointCollection


pytestmark = pytest.mark.asyncio

async def test_recovery_points_get(client):
    """Test case for recovery_points_get

    Get a recovery point.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationFabrics/{fabric_name}/replicationProtectionContainers/{protection_container_name}/replicationProtectedItems/{replicated_protected_item_name}/recoveryPoints/{recovery_point_name}'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', fabric_name='fabric_name_example', protection_container_name='protection_container_name_example', replicated_protected_item_name='replicated_protected_item_name_example', recovery_point_name='recovery_point_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recovery_points_list_by_replication_protected_items(client):
    """Test case for recovery_points_list_by_replication_protected_items

    Get recovery points for a replication protected item.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationFabrics/{fabric_name}/replicationProtectionContainers/{protection_container_name}/replicationProtectedItems/{replicated_protected_item_name}/recoveryPoints'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', fabric_name='fabric_name_example', protection_container_name='protection_container_name_example', replicated_protected_item_name='replicated_protected_item_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


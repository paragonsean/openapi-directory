# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.target_compute_size_collection import TargetComputeSizeCollection


pytestmark = pytest.mark.asyncio

async def test_target_compute_sizes_list_by_replication_protected_items(client):
    """Test case for target_compute_sizes_list_by_replication_protected_items

    Gets the list of target compute sizes for the replication protected item.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationFabrics/{fabric_name}/replicationProtectionContainers/{protection_container_name}/replicationProtectedItems/{replicated_protected_item_name}/targetComputeSizes'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', fabric_name='fabric_name_example', protection_container_name='protection_container_name_example', replicated_protected_item_name='replicated_protected_item_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


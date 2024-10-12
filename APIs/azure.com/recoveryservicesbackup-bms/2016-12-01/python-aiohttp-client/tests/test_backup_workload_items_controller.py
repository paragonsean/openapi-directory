# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.workload_item_resource_list import WorkloadItemResourceList


pytestmark = pytest.mark.asyncio

async def test_backup_workload_items_list(client):
    """Test case for backup_workload_items_list

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example'),
                    ('$skipToken', 'skip_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{vault_name}/backupFabrics/{fabric_name}/protectionContainers/{container_name}/items'.format(vault_name='vault_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', fabric_name='fabric_name_example', container_name='container_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.storage_pool import StoragePool
from openapi_server.models.storage_pool_list import StoragePoolList


pytestmark = pytest.mark.asyncio

async def test_storage_pools_get(client):
    """Test case for storage_pools_get

    
    """
    params = [('api-version', '2016-05-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/storageSubSystems/{storage_sub_system}/storagePools/{storage_pool}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', location='location_example', storage_sub_system='storage_sub_system_example', storage_pool='storage_pool_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_pools_list(client):
    """Test case for storage_pools_list

    
    """
    params = [('api-version', '2016-05-01'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/storageSubSystems/{storage_sub_system}/storagePools'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', location='location_example', storage_sub_system='storage_sub_system_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


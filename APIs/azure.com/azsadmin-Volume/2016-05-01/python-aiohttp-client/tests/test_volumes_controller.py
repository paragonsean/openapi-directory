# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.volume import Volume
from openapi_server.models.volume_list import VolumeList


pytestmark = pytest.mark.asyncio

async def test_volumes_get(client):
    """Test case for volumes_get

    
    """
    params = [('api-version', '2016-05-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/storageSubSystems/{storage_sub_system}/storagePools/{storage_pool}/volumes/{volume}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', location='location_example', storage_sub_system='storage_sub_system_example', storage_pool='storage_pool_example', volume='volume_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_volumes_list(client):
    """Test case for volumes_list

    
    """
    params = [('api-version', '2016-05-01'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/storageSubSystems/{storage_sub_system}/storagePools/{storage_pool}/volumes'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', location='location_example', storage_sub_system='storage_sub_system_example', storage_pool='storage_pool_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


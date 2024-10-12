# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.storage_system import StorageSystem
from openapi_server.models.storage_system_list import StorageSystemList


pytestmark = pytest.mark.asyncio

async def test_storage_systems_get(client):
    """Test case for storage_systems_get

    
    """
    params = [('api-version', '2016-05-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/storageSubSystems/{storage_sub_system}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', location='location_example', storage_sub_system='storage_sub_system_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_systems_list(client):
    """Test case for storage_systems_list

    
    """
    params = [('api-version', '2016-05-01'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/storageSubSystems'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', location='location_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


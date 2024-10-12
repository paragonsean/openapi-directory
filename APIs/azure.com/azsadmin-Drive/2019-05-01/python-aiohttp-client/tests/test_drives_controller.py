# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.drive import Drive
from openapi_server.models.drive_list import DriveList


pytestmark = pytest.mark.asyncio

async def test_drives_get(client):
    """Test case for drives_get

    
    """
    params = [('api-version', '2019-05-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/scaleUnits/{scale_unit}/storageSubSystems/{storage_sub_system}/drives/{drive}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', location='location_example', scale_unit='scale_unit_example', storage_sub_system='storage_sub_system_example', drive='drive_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drives_list(client):
    """Test case for drives_list

    
    """
    params = [('api-version', '2019-05-01'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/scaleUnits/{scale_unit}/storageSubSystems/{storage_sub_system}/drives'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', location='location_example', scale_unit='scale_unit_example', storage_sub_system='storage_sub_system_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


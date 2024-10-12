# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.na_device_list_response import NADeviceListResponse
from openapi_server.models.na_therm_state_response import NAThermStateResponse
from openapi_server.models.na_user_response import NAUserResponse


pytestmark = pytest.mark.asyncio

async def test_devicelist(client):
    """Test case for devicelist

    
    """
    params = [('app_type', 'app_type_example'),
                    ('device_id', 'device_id_example'),
                    ('get_favorites', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/devicelist',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_getthermstate(client):
    """Test case for getthermstate

    
    """
    params = [('device_id', 'device_id_example'),
                    ('module_id', 'module_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/getthermstate',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_getuser(client):
    """Test case for getuser

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/getuser',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


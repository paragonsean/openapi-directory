# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.device_create_request import DeviceCreateRequest
from openapi_server.models.device_response import DeviceResponse
from openapi_server.models.device_update_request import DeviceUpdateRequest
from openapi_server.models.devices_response import DevicesResponse
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_devices_create_instance(client):
    """Test case for devices_create_instance

    
    """
    body = {"data":{"attributes":{"name":"name","udid":"udid","platform":"IOS"},"type":"devices"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/devices',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_devices_get_collection(client):
    """Test case for devices_get_collection

    
    """
    params = [('filter[name]', ['filter_name_example']),
                    ('filter[platform]', ['filter_platform_example']),
                    ('filter[status]', ['filter_status_example']),
                    ('filter[udid]', ['filter_udid_example']),
                    ('filter[id]', ['filter_id_example']),
                    ('sort', ['sort_example']),
                    ('fields[devices]', ['fields_devices_example']),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/devices',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_devices_get_instance(client):
    """Test case for devices_get_instance

    
    """
    params = [('fields[devices]', ['fields_devices_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/devices/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_devices_update_instance(client):
    """Test case for devices_update_instance

    
    """
    body = {"data":{"attributes":{"name":"name","status":"ENABLED"},"id":"id","type":"devices"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/devices/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


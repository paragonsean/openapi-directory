# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_device_config_response import ListDeviceConfigResponse
from openapi_server.models.microvisor_v1_device_device_config import MicrovisorV1DeviceDeviceConfig


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_device_config(client):
    """Test case for create_device_config

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'key': 'key_example',
        'value': 'value_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Devices/{device_sid}/Configs'.format(device_sid='device_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_device_config(client):
    """Test case for delete_device_config

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/Devices/{device_sid}/Configs/{key}'.format(device_sid='device_sid_example', key='key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_device_config(client):
    """Test case for fetch_device_config

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Devices/{device_sid}/Configs/{key}'.format(device_sid='device_sid_example', key='key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_device_config(client):
    """Test case for list_device_config

    
    """
    params = [('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Devices/{device_sid}/Configs'.format(device_sid='device_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_device_config(client):
    """Test case for update_device_config

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'value': 'value_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Devices/{device_sid}/Configs/{key}'.format(device_sid='device_sid_example', key='key_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


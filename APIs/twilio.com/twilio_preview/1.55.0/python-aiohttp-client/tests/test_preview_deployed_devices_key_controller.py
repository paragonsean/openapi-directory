# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_deployed_devices_key_response import ListDeployedDevicesKeyResponse
from openapi_server.models.preview_deployed_devices_fleet_key import PreviewDeployedDevicesFleetKey


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_deployed_devices_key(client):
    """Test case for create_deployed_devices_key

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'device_sid': 'device_sid_example',
        'friendly_name': 'friendly_name_example'
        }
    response = await client.request(
        method='POST',
        path='/DeployedDevices/Fleets/{fleet_sid}/Keys'.format(fleet_sid='fleet_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_deployed_devices_key(client):
    """Test case for delete_deployed_devices_key

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/DeployedDevices/Fleets/{fleet_sid}/Keys/{sid}'.format(fleet_sid='fleet_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_deployed_devices_key(client):
    """Test case for fetch_deployed_devices_key

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/DeployedDevices/Fleets/{fleet_sid}/Keys/{sid}'.format(fleet_sid='fleet_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_deployed_devices_key(client):
    """Test case for list_deployed_devices_key

    
    """
    params = [('DeviceSid', 'device_sid_example'),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/DeployedDevices/Fleets/{fleet_sid}/Keys'.format(fleet_sid='fleet_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_deployed_devices_key(client):
    """Test case for update_deployed_devices_key

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'device_sid': 'device_sid_example',
        'friendly_name': 'friendly_name_example'
        }
    response = await client.request(
        method='POST',
        path='/DeployedDevices/Fleets/{fleet_sid}/Keys/{sid}'.format(fleet_sid='fleet_sid_example', sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


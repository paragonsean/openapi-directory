# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.device_info import DeviceInfo
from openapi_server.models.device_info_query_result import DeviceInfoQueryResult
from openapi_server.models.device_options import DeviceOptions
from openapi_server.models.problem_details import ProblemDetails


pytestmark = pytest.mark.asyncio

async def test_delete_device(client):
    """Test case for delete_device

    Deletes a device.
    """
    params = [('id', 'id_example')]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/Devices',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_device_info(client):
    """Test case for get_device_info

    Get info for a device.
    """
    params = [('id', 'id_example')]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Devices/Info',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_device_options(client):
    """Test case for get_device_options

    Get options for a device.
    """
    params = [('id', 'id_example')]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Devices/Options',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_devices(client):
    """Test case for get_devices

    Get Devices.
    """
    params = [('supportsSync', True),
                    ('userId', 'user_id_example')]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Devices',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update_device_options(client):
    """Test case for update_device_options

    Update device options.
    """
    body = {"CustomName":"CustomName"}
    params = [('id', 'id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Devices/Options',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


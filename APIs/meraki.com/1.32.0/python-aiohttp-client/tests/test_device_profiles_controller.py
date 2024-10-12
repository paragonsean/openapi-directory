# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_network_sm_device_device_profiles200_response_inner import GetNetworkSmDeviceDeviceProfiles200ResponseInner


pytestmark = pytest.mark.asyncio

async def test_get_network_sm_device_device_profiles_2(client):
    """Test case for get_network_sm_device_device_profiles_2

    Get the installed profiles associated with a device
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/sm/devices/{device_id}/deviceProfiles'.format(network_id='network_id_example', device_id='device_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_sm_user_device_profiles_2(client):
    """Test case for get_network_sm_user_device_profiles_2

    Get the profiles associated with a user
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/sm/users/{user_id}/deviceProfiles'.format(network_id='network_id_example', user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


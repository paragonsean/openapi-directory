# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_network_camera_wireless_profile_request import CreateNetworkCameraWirelessProfileRequest
from openapi_server.models.update_device_camera_wireless_profiles_request import UpdateDeviceCameraWirelessProfilesRequest
from openapi_server.models.update_network_camera_wireless_profile_request import UpdateNetworkCameraWirelessProfileRequest


pytestmark = pytest.mark.asyncio

async def test_create_network_camera_wireless_profile_1(client):
    """Test case for create_network_camera_wireless_profile_1

    Creates a new camera wireless profile for this network.
    """
    body = openapi_server.CreateNetworkCameraWirelessProfileRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/camera/wirelessProfiles'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_network_camera_wireless_profile_1(client):
    """Test case for delete_network_camera_wireless_profile_1

    Delete an existing camera wireless profile for this network.
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/networks/{network_id}/camera/wirelessProfiles/{wireless_profile_id}'.format(network_id='network_id_example', wireless_profile_id='wireless_profile_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_device_camera_wireless_profiles_1(client):
    """Test case for get_device_camera_wireless_profiles_1

    Returns wireless profile assigned to the given camera
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/devices/{serial}/camera/wirelessProfiles'.format(serial='serial_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_camera_wireless_profile_1(client):
    """Test case for get_network_camera_wireless_profile_1

    Retrieve a single camera wireless profile.
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/camera/wirelessProfiles/{wireless_profile_id}'.format(network_id='network_id_example', wireless_profile_id='wireless_profile_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_camera_wireless_profiles_1(client):
    """Test case for get_network_camera_wireless_profiles_1

    List the camera wireless profiles for this network.
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/camera/wirelessProfiles'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_device_camera_wireless_profiles_1(client):
    """Test case for update_device_camera_wireless_profiles_1

    Assign wireless profiles to the given camera
    """
    body = openapi_server.UpdateDeviceCameraWirelessProfilesRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/devices/{serial}/camera/wirelessProfiles'.format(serial='serial_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_camera_wireless_profile_1(client):
    """Test case for update_network_camera_wireless_profile_1

    Update an existing camera wireless profile in this network.
    """
    body = openapi_server.UpdateNetworkCameraWirelessProfileRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/camera/wirelessProfiles/{wireless_profile_id}'.format(network_id='network_id_example', wireless_profile_id='wireless_profile_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


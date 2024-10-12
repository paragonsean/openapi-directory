# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.generate_network_camera_snapshot_request import GenerateNetworkCameraSnapshotRequest
from openapi_server.models.update_device_camera_video_settings_request import UpdateDeviceCameraVideoSettingsRequest


pytestmark = pytest.mark.asyncio

async def test_generate_network_camera_snapshot(client):
    """Test case for generate_network_camera_snapshot

    Generate a snapshot of what the camera sees at the specified time and return a link to that image.
    """
    body = openapi_server.GenerateNetworkCameraSnapshotRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v0/networks/{network_id}/cameras/{serial}/snapshot'.format(network_id='network_id_example', serial='serial_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_device_camera_video_settings(client):
    """Test case for get_device_camera_video_settings

    Returns video settings for the given camera
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/devices/{serial}/camera/video/settings'.format(serial='serial_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_camera_schedules(client):
    """Test case for get_network_camera_schedules

    Returns a list of all camera recording schedules.
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/camera/schedules'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_camera_video_link(client):
    """Test case for get_network_camera_video_link

    Returns video link to the specified camera
    """
    params = [('timestamp', 'timestamp_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/cameras/{serial}/videoLink'.format(network_id='network_id_example', serial='serial_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_device_camera_video_settings(client):
    """Test case for update_device_camera_video_settings

    Update video settings for the given camera
    """
    body = openapi_server.UpdateDeviceCameraVideoSettingsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v0/devices/{serial}/camera/video/settings'.format(serial='serial_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


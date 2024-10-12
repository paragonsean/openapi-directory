# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.update_device_camera_quality_and_retention_request import UpdateDeviceCameraQualityAndRetentionRequest


pytestmark = pytest.mark.asyncio

async def test_get_device_camera_quality_and_retention_1(client):
    """Test case for get_device_camera_quality_and_retention_1

    Returns quality and retention settings for the given camera
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/devices/{serial}/camera/qualityAndRetention'.format(serial='serial_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_device_camera_quality_and_retention_1(client):
    """Test case for update_device_camera_quality_and_retention_1

    Update quality and retention settings for the given camera
    """
    body = openapi_server.UpdateDeviceCameraQualityAndRetentionRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/devices/{serial}/camera/qualityAndRetention'.format(serial='serial_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


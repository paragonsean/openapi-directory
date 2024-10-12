# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.update_device_camera_sense_request import UpdateDeviceCameraSenseRequest


pytestmark = pytest.mark.asyncio

async def test_get_device_camera_sense_1(client):
    """Test case for get_device_camera_sense_1

    Returns sense settings for a given camera
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/devices/{serial}/camera/sense'.format(serial='serial_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_device_camera_sense_object_detection_models_1(client):
    """Test case for get_device_camera_sense_object_detection_models_1

    Returns the MV Sense object detection model list for the given camera
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/devices/{serial}/camera/sense/objectDetectionModels'.format(serial='serial_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_device_camera_sense_1(client):
    """Test case for update_device_camera_sense_1

    Update sense settings for the given camera
    """
    body = openapi_server.UpdateDeviceCameraSenseRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/devices/{serial}/camera/sense'.format(serial='serial_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


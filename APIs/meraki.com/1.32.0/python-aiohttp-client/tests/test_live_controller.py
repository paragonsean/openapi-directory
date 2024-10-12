# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_device_camera_analytics_live_2(client):
    """Test case for get_device_camera_analytics_live_2

    Returns live state from camera of analytics zones
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/devices/{serial}/camera/analytics/live'.format(serial='serial_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


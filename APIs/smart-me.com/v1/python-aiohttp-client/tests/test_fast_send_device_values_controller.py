# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_fast_send_device_values_get(client):
    """Test case for fast_send_device_values_get

    Force a device to send the data every second (if supported). This for about 30s.              Don't use this call to force a device to send the data every second for a longer time.
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/FastSendDeviceValues/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


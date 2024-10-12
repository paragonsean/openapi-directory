# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.device import Device


pytestmark = pytest.mark.asyncio

async def test_device_by_serial_get(client):
    """Test case for device_by_serial_get

    Gets a Device by it's Serial Number. The Serial is the part before the \"-\".
    """
    params = [('serial', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/DeviceBySerial',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


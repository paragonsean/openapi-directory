# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.device import Device


pytestmark = pytest.mark.asyncio

async def test_devices_by_sub_type_get(client):
    """Test case for devices_by_sub_type_get

    Gets all Devices by it's Sub Type (e.g. E-Charging Station)
    """
    params = [('meterSubType', 'meter_sub_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/DevicesBySubType',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


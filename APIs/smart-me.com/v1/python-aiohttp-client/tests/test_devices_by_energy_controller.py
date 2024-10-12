# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.device import Device


pytestmark = pytest.mark.asyncio

async def test_devices_by_energy_get(client):
    """Test case for devices_by_energy_get

    Gets all Devices for an Energy Type
    """
    params = [('meterEnergyType', 'meter_energy_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/DevicesByEnergy',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


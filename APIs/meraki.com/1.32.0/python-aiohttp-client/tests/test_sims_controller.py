# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.update_device_cellular_sims_request import UpdateDeviceCellularSimsRequest


pytestmark = pytest.mark.asyncio

async def test_get_device_cellular_sims_2(client):
    """Test case for get_device_cellular_sims_2

    Return the SIM and APN configurations for a cellular device.
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/devices/{serial}/cellular/sims'.format(serial='serial_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_device_cellular_sims_2(client):
    """Test case for update_device_cellular_sims_2

    Updates the SIM and APN configurations for a cellular device.
    """
    body = openapi_server.UpdateDeviceCellularSimsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/devices/{serial}/cellular/sims'.format(serial='serial_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


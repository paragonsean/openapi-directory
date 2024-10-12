# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.device_in_past import DeviceInPast


pytestmark = pytest.mark.asyncio

async def test_meter_values_get(client):
    """Test case for meter_values_get

    Gets the Values for a Meter at a given Date.               The first Value found before the given Date is returned.
    """
    params = [('date', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/MeterValues/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


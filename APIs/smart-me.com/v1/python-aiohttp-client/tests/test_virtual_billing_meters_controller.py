# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.device import Device


pytestmark = pytest.mark.asyncio

async def test_virtual_billing_meters_get(client):
    """Test case for virtual_billing_meters_get

    Beta: Gets all Meters available to activate as a Virtual Meter.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/VirtualBillingMeters',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


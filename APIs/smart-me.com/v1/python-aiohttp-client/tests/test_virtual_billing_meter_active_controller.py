# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.device import Device
from openapi_server.models.v_meter_to_activate import VMeterToActivate


pytestmark = pytest.mark.asyncio

async def test_virtual_billing_meter_active_get(client):
    """Test case for virtual_billing_meter_active_get

    Beta: Gets all active virtual meters
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/VirtualBillingMeterActive',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_virtual_billing_meter_active_post(client):
    """Test case for virtual_billing_meter_active_post

    Beta: Virtual Meter API: Activates a Meter and add the Consumption to a Virtual Meter assosiated with the User.
    """
    body = {"SerialNumber":"SerialNumber"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/VirtualBillingMeterActive',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.v_meter_to_deactivate import VMeterToDeactivate


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_virtual_billing_meter_deactivate_post(client):
    """Test case for virtual_billing_meter_deactivate_post

    Beta: Virtual Meter API: Deactivates a Virtual Meter.
    """
    body = {"ID":"ID"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/VirtualBillingMeterDeactivate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


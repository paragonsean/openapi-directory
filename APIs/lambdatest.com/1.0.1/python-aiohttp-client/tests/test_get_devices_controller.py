# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.access_denied import AccessDenied
from openapi_server.models.os_devices import OsDevices


pytestmark = pytest.mark.asyncio

async def test_devices(client):
    """Test case for devices

    Fetch all available device combinations.
    """
    params = [('os', 'os_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/screenshots/v1/devices',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


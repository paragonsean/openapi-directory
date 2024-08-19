# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.uptime_check import UptimeCheck


pytestmark = pytest.mark.asyncio

async def test_uptime_checks_get_all(client):
    """Test case for uptime_checks_get_all

    Fetch a list of uptime checks. Currently in closed beta. Get in contact to get access to this endpoint.
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/uptimechecks',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.device import Device


pytestmark = pytest.mark.asyncio

async def test_pico_get(client):
    """Test case for pico_get

    Gets all pico charging stations for this user
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/pico',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


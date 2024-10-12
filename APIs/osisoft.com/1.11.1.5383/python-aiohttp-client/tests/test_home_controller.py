# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.landing import Landing


pytestmark = pytest.mark.asyncio

async def test_home_get(client):
    """Test case for home_get

    Get top level links for this PI System Web API instance.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


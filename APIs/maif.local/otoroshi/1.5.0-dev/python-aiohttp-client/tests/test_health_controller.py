# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.otoroshi_health import OtoroshiHealth


pytestmark = pytest.mark.asyncio

async def test_health(client):
    """Test case for health

    Return current Otoroshi health
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/health',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


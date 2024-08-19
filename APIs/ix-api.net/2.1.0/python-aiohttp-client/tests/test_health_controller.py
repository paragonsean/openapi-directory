# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.health_response import HealthResponse


pytestmark = pytest.mark.asyncio

async def test_api_health_read(client):
    """Test case for api_health_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/health',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


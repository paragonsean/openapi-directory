# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.health_check200_response import HealthCheck200Response


pytestmark = pytest.mark.asyncio

async def test_health_check(client):
    """Test case for health_check

    /health/check
    """
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'en-US',
        'Legacy-API-key': 'special-key',
        'API-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/service/health/check',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


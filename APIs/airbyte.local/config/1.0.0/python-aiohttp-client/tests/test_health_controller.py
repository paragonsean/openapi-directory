# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.health_check_read import HealthCheckRead


pytestmark = pytest.mark.asyncio

async def test_get_health_check(client):
    """Test case for get_health_check

    Health Check
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/health',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


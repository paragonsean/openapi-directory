# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.health_check import HealthCheck


pytestmark = pytest.mark.asyncio

async def test_get_health_check(client):
    """Test case for get_health_check

    Get health check status
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Healthcheck',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.health_check import HealthCheck


pytestmark = pytest.mark.asyncio

async def test_get_health(client):
    """Test case for get_health

    Get the health of an instance
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/health',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


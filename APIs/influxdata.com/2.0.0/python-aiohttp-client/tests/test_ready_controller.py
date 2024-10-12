# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.ready import Ready


pytestmark = pytest.mark.asyncio

async def test_get_ready(client):
    """Test case for get_ready

    Get the readiness of an instance at startup
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/ready',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


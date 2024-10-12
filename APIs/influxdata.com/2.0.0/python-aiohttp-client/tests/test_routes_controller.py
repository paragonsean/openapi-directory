# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.routes import Routes


pytestmark = pytest.mark.asyncio

async def test_get_routes(client):
    """Test case for get_routes

    List all top level routes
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


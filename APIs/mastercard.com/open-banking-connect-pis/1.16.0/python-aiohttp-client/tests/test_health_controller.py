# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_health import ApiHealth
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_payments_health_get(client):
    """Test case for payments_health_get

    Returns the status of each connectivity provider
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/openbanking/sandbox/connect/api/payments/health',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.basic_error import BasicError
from openapi_server.models.rate_limit_overview import RateLimitOverview


pytestmark = pytest.mark.asyncio

async def test_rate_limit_get(client):
    """Test case for rate_limit_get

    Get rate limit status for the authenticated user
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/rate_limit',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


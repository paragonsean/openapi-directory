# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.rate_limits_response import RateLimitsResponse


pytestmark = pytest.mark.asyncio

async def test_get_user_rate_limits(client):
    """Test case for get_user_rate_limits

    
    """
    params = [('api_context', 'api_context_example'),
                    ('api_name', 'api_name_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/developer/analytics/v1_beta/user_rate_limit/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


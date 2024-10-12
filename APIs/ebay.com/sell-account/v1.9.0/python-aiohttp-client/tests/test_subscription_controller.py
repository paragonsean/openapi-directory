# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.subscription_response import SubscriptionResponse


pytestmark = pytest.mark.asyncio

async def test_get_subscription(client):
    """Test case for get_subscription

    
    """
    params = [('limit', 'limit_example'),
                    ('continuation_token', 'continuation_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/account/v1/subscription',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


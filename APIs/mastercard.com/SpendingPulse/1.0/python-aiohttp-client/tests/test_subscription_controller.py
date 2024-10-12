# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_schema import ErrorSchema
from openapi_server.models.subscription_list_response import SubscriptionListResponse


pytestmark = pytest.mark.asyncio

async def test_subscription_get(client):
    """Test case for subscription_get

    Returns a list of all reports one is currently subscribed to.
    """
    params = [('CurrentRow', '1'),
                    ('Offset', '25')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/spendingpulse/v1/spulse.svc/subscription',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


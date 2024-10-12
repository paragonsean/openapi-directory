# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.subscription import Subscription


pytestmark = pytest.mark.asyncio

async def test_get_subscription(client):
    """Test case for get_subscription

    Retrieve subscription details
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscription.{content_type}'.format(content_type='content_type_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


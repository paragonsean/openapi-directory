# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_conversation import GetConversation


pytestmark = pytest.mark.asyncio

async def test_get_conversation(client):
    """Test case for get_conversation

    Retrieve order conversation
    """
    params = [('reason', 'data-validation')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/oms/pvt/orders/{order_id}/conversation-message'.format(order_id='1172452900788-01'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


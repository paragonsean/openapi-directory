# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.conversations_call import ConversationsCall


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v2_conversations_calls_post(client):
    """Test case for v2_conversations_calls_post

    Create Conversations Call
    """
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'call_created_at': 'call_created_at_example',
        'direction': 'direction_example',
        'duration': 3.4,
        '_from': '_from_example',
        'recording': None,
        'to': 'to_example',
        'user_guid': 'user_guid_example'
        }
    response = await client.request(
        method='POST',
        path='/v2/conversations/calls',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


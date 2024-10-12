# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_conversations200_response import GetConversations200Response


pytestmark = pytest.mark.asyncio

async def test_get_conversations(client):
    """Test case for get_conversations

    List Conversations
    """
    params = [('page_size', 10),
                    ('order', asc),
                    ('cursor', 'cursor_example'),
                    ('date_start', 'date_start_example'),
                    ('date_end', 'date_end_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v0.2/conversations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


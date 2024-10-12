# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.chat_scheduled_messages_list_error_schema import ChatScheduledMessagesListErrorSchema
from openapi_server.models.chat_scheduled_messages_list_schema import ChatScheduledMessagesListSchema


pytestmark = pytest.mark.asyncio

async def test_chat_scheduled_messages_list(client):
    """Test case for chat_scheduled_messages_list

    
    """
    params = [('channel', 'channel_example'),
                    ('latest', 3.4),
                    ('oldest', 3.4),
                    ('limit', 56),
                    ('cursor', 'cursor_example')]
    headers = { 
        'Accept': 'application/json',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/chat.scheduledMessages.list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


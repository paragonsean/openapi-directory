# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.conversation_response import ConversationResponse
from openapi_server.models.conversations_response import ConversationsResponse
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_conversations_close(client):
    """Test case for conversations_close

    Closes a conversation
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/accounts/{account_id}/conversations/{conversation_id}/close'.format(account_id='account_id_example', conversation_id='conversation_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_conversations_fetch(client):
    """Test case for conversations_fetch

    Fetch conversation by ID
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/accounts/{account_id}/conversations/{conversation_id}'.format(account_id='account_id_example', conversation_id='conversation_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_conversations_fetch_all(client):
    """Test case for conversations_fetch_all

    Fetch conversations
    """
    params = [('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/accounts/{account_id}/conversations'.format(account_id='account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.conversations_conversation_id_offer_post_request import ConversationsConversationIdOfferPostRequest
from openapi_server.models.conversations_id_offer_post_request import ConversationsIdOfferPostRequest


pytestmark = pytest.mark.asyncio

async def test_conversations_conversation_id_offer_post(client):
    """Test case for conversations_conversation_id_offer_post

    Make an offer to the other participant in the conversation
    """
    body = openapi_server.ConversationsConversationIdOfferPostRequest()
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/conversations/{conversation_id}/offer'.format(conversation_id='conversation_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_conversations_id_offer_post(client):
    """Test case for conversations_id_offer_post

    Make an offer to the other participant in the conversation
    """
    body = openapi_server.ConversationsIdOfferPostRequest()
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/conversations/{id}/offer'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


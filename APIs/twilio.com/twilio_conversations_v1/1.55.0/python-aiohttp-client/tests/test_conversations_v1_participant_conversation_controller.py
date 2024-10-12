# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_participant_conversation_response import ListParticipantConversationResponse
from openapi_server.models.list_service_participant_conversation_response import ListServiceParticipantConversationResponse


pytestmark = pytest.mark.asyncio

async def test_list_participant_conversation(client):
    """Test case for list_participant_conversation

    
    """
    params = [('Identity', 'identity_example'),
                    ('Address', 'address_example'),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/ParticipantConversations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_service_participant_conversation(client):
    """Test case for list_service_participant_conversation

    
    """
    params = [('Identity', 'identity_example'),
                    ('Address', 'address_example'),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Services/{chat_service_sid}/ParticipantConversations'.format(chat_service_sid='chat_service_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


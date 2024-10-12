# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.conversations_v1_conversation_conversation_message_conversation_message_receipt import ConversationsV1ConversationConversationMessageConversationMessageReceipt
from openapi_server.models.conversations_v1_service_service_conversation_service_conversation_message_service_conversation_message_receipt import ConversationsV1ServiceServiceConversationServiceConversationMessageServiceConversationMessageReceipt
from openapi_server.models.list_conversation_message_receipt_response import ListConversationMessageReceiptResponse
from openapi_server.models.list_service_conversation_message_receipt_response import ListServiceConversationMessageReceiptResponse


pytestmark = pytest.mark.asyncio

async def test_fetch_conversation_message_receipt(client):
    """Test case for fetch_conversation_message_receipt

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Conversations/{conversation_sid}/Messages/{message_sid}/Receipts/{sid}'.format(conversation_sid='conversation_sid_example', message_sid='message_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_service_conversation_message_receipt(client):
    """Test case for fetch_service_conversation_message_receipt

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Messages/{message_sid}/Receipts/{sid}'.format(chat_service_sid='chat_service_sid_example', conversation_sid='conversation_sid_example', message_sid='message_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_conversation_message_receipt(client):
    """Test case for list_conversation_message_receipt

    
    """
    params = [('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Conversations/{conversation_sid}/Messages/{message_sid}/Receipts'.format(conversation_sid='conversation_sid_example', message_sid='message_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_service_conversation_message_receipt(client):
    """Test case for list_service_conversation_message_receipt

    
    """
    params = [('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Messages/{message_sid}/Receipts'.format(chat_service_sid='chat_service_sid_example', conversation_sid='conversation_sid_example', message_sid='message_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


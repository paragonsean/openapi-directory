# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.conversations_v1_service_service_user_service_user_conversation import ConversationsV1ServiceServiceUserServiceUserConversation
from openapi_server.models.conversations_v1_user_user_conversation import ConversationsV1UserUserConversation
from openapi_server.models.list_service_user_conversation_response import ListServiceUserConversationResponse
from openapi_server.models.list_user_conversation_response import ListUserConversationResponse
from openapi_server.models.service_user_conversation_enum_notification_level import ServiceUserConversationEnumNotificationLevel
from openapi_server.models.user_conversation_enum_notification_level import UserConversationEnumNotificationLevel


pytestmark = pytest.mark.asyncio

async def test_delete_service_user_conversation(client):
    """Test case for delete_service_user_conversation

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/Services/{chat_service_sid}/Users/{user_sid}/Conversations/{conversation_sid}'.format(chat_service_sid='chat_service_sid_example', user_sid='user_sid_example', conversation_sid='conversation_sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_user_conversation(client):
    """Test case for delete_user_conversation

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/Users/{user_sid}/Conversations/{conversation_sid}'.format(user_sid='user_sid_example', conversation_sid='conversation_sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_service_user_conversation(client):
    """Test case for fetch_service_user_conversation

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Services/{chat_service_sid}/Users/{user_sid}/Conversations/{conversation_sid}'.format(chat_service_sid='chat_service_sid_example', user_sid='user_sid_example', conversation_sid='conversation_sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_user_conversation(client):
    """Test case for fetch_user_conversation

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Users/{user_sid}/Conversations/{conversation_sid}'.format(user_sid='user_sid_example', conversation_sid='conversation_sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_service_user_conversation(client):
    """Test case for list_service_user_conversation

    
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
        path='/v1/Services/{chat_service_sid}/Users/{user_sid}/Conversations'.format(chat_service_sid='chat_service_sid_example', user_sid='user_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_user_conversation(client):
    """Test case for list_user_conversation

    
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
        path='/v1/Users/{user_sid}/Conversations'.format(user_sid='user_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_service_user_conversation(client):
    """Test case for update_service_user_conversation

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'last_read_message_index': 56,
        'last_read_timestamp': '2013-10-20T19:20:30+01:00',
        'notification_level': openapi_server.ServiceUserConversationEnumNotificationLevel()
        }
    response = await client.request(
        method='POST',
        path='/v1/Services/{chat_service_sid}/Users/{user_sid}/Conversations/{conversation_sid}'.format(chat_service_sid='chat_service_sid_example', user_sid='user_sid_example', conversation_sid='conversation_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_user_conversation(client):
    """Test case for update_user_conversation

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'last_read_message_index': 56,
        'last_read_timestamp': '2013-10-20T19:20:30+01:00',
        'notification_level': openapi_server.UserConversationEnumNotificationLevel()
        }
    response = await client.request(
        method='POST',
        path='/v1/Users/{user_sid}/Conversations/{conversation_sid}'.format(user_sid='user_sid_example', conversation_sid='conversation_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


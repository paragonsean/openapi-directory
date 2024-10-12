# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.conversation_enum_state import ConversationEnumState
from openapi_server.models.conversation_enum_webhook_enabled_type import ConversationEnumWebhookEnabledType
from openapi_server.models.conversations_v1_conversation import ConversationsV1Conversation
from openapi_server.models.conversations_v1_service_service_conversation import ConversationsV1ServiceServiceConversation
from openapi_server.models.list_conversation_response import ListConversationResponse
from openapi_server.models.list_service_conversation_response import ListServiceConversationResponse
from openapi_server.models.service_conversation_enum_state import ServiceConversationEnumState
from openapi_server.models.service_conversation_enum_webhook_enabled_type import ServiceConversationEnumWebhookEnabledType


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_conversation(client):
    """Test case for create_conversation

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'x_twilio_webhook_enabled': openapi_server.ConversationEnumWebhookEnabledType(),
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'attributes': 'attributes_example',
        'bindings_email_address': 'bindings_email_address_example',
        'bindings_email_name': 'bindings_email_name_example',
        'date_created': '2013-10-20T19:20:30+01:00',
        'date_updated': '2013-10-20T19:20:30+01:00',
        'friendly_name': 'friendly_name_example',
        'messaging_service_sid': 'messaging_service_sid_example',
        'state': openapi_server.ConversationEnumState(),
        'timers_closed': 'timers_closed_example',
        'timers_inactive': 'timers_inactive_example',
        'unique_name': 'unique_name_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Conversations',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_service_conversation(client):
    """Test case for create_service_conversation

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'x_twilio_webhook_enabled': openapi_server.ServiceConversationEnumWebhookEnabledType(),
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'attributes': 'attributes_example',
        'bindings_email_address': 'bindings_email_address_example',
        'bindings_email_name': 'bindings_email_name_example',
        'date_created': '2013-10-20T19:20:30+01:00',
        'date_updated': '2013-10-20T19:20:30+01:00',
        'friendly_name': 'friendly_name_example',
        'messaging_service_sid': 'messaging_service_sid_example',
        'state': openapi_server.ServiceConversationEnumState(),
        'timers_closed': 'timers_closed_example',
        'timers_inactive': 'timers_inactive_example',
        'unique_name': 'unique_name_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Services/{chat_service_sid}/Conversations'.format(chat_service_sid='chat_service_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_conversation(client):
    """Test case for delete_conversation

    
    """
    headers = { 
        'x_twilio_webhook_enabled': openapi_server.ConversationEnumWebhookEnabledType(),
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/Conversations/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_service_conversation(client):
    """Test case for delete_service_conversation

    
    """
    headers = { 
        'x_twilio_webhook_enabled': openapi_server.ServiceConversationEnumWebhookEnabledType(),
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/Services/{chat_service_sid}/Conversations/{sid}'.format(chat_service_sid='chat_service_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_conversation(client):
    """Test case for fetch_conversation

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Conversations/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_service_conversation(client):
    """Test case for fetch_service_conversation

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Services/{chat_service_sid}/Conversations/{sid}'.format(chat_service_sid='chat_service_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_conversation(client):
    """Test case for list_conversation

    
    """
    params = [('StartDate', 'start_date_example'),
                    ('EndDate', 'end_date_example'),
                    ('State', openapi_server.ConversationEnumState()),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Conversations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_service_conversation(client):
    """Test case for list_service_conversation

    
    """
    params = [('StartDate', 'start_date_example'),
                    ('EndDate', 'end_date_example'),
                    ('State', openapi_server.ServiceConversationEnumState()),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Services/{chat_service_sid}/Conversations'.format(chat_service_sid='chat_service_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_conversation(client):
    """Test case for update_conversation

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'x_twilio_webhook_enabled': openapi_server.ConversationEnumWebhookEnabledType(),
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'attributes': 'attributes_example',
        'bindings_email_address': 'bindings_email_address_example',
        'bindings_email_name': 'bindings_email_name_example',
        'date_created': '2013-10-20T19:20:30+01:00',
        'date_updated': '2013-10-20T19:20:30+01:00',
        'friendly_name': 'friendly_name_example',
        'messaging_service_sid': 'messaging_service_sid_example',
        'state': openapi_server.ConversationEnumState(),
        'timers_closed': 'timers_closed_example',
        'timers_inactive': 'timers_inactive_example',
        'unique_name': 'unique_name_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Conversations/{sid}'.format(sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_service_conversation(client):
    """Test case for update_service_conversation

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'x_twilio_webhook_enabled': openapi_server.ServiceConversationEnumWebhookEnabledType(),
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'attributes': 'attributes_example',
        'bindings_email_address': 'bindings_email_address_example',
        'bindings_email_name': 'bindings_email_name_example',
        'date_created': '2013-10-20T19:20:30+01:00',
        'date_updated': '2013-10-20T19:20:30+01:00',
        'friendly_name': 'friendly_name_example',
        'messaging_service_sid': 'messaging_service_sid_example',
        'state': openapi_server.ServiceConversationEnumState(),
        'timers_closed': 'timers_closed_example',
        'timers_inactive': 'timers_inactive_example',
        'unique_name': 'unique_name_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Services/{chat_service_sid}/Conversations/{sid}'.format(chat_service_sid='chat_service_sid_example', sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


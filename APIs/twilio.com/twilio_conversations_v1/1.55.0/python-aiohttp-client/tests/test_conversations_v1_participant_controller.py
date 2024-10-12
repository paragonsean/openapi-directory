# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.conversation_participant_enum_webhook_enabled_type import ConversationParticipantEnumWebhookEnabledType
from openapi_server.models.conversations_v1_conversation_conversation_participant import ConversationsV1ConversationConversationParticipant
from openapi_server.models.conversations_v1_service_service_conversation_service_conversation_participant import ConversationsV1ServiceServiceConversationServiceConversationParticipant
from openapi_server.models.list_conversation_participant_response import ListConversationParticipantResponse
from openapi_server.models.list_service_conversation_participant_response import ListServiceConversationParticipantResponse
from openapi_server.models.service_conversation_participant_enum_webhook_enabled_type import ServiceConversationParticipantEnumWebhookEnabledType


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_conversation_participant(client):
    """Test case for create_conversation_participant

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'x_twilio_webhook_enabled': openapi_server.ConversationParticipantEnumWebhookEnabledType(),
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'attributes': 'attributes_example',
        'date_created': '2013-10-20T19:20:30+01:00',
        'date_updated': '2013-10-20T19:20:30+01:00',
        'identity': 'identity_example',
        'messaging_binding_address': 'messaging_binding_address_example',
        'messaging_binding_projected_address': 'messaging_binding_projected_address_example',
        'messaging_binding_proxy_address': 'messaging_binding_proxy_address_example',
        'role_sid': 'role_sid_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Conversations/{conversation_sid}/Participants'.format(conversation_sid='conversation_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_service_conversation_participant(client):
    """Test case for create_service_conversation_participant

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'x_twilio_webhook_enabled': openapi_server.ServiceConversationParticipantEnumWebhookEnabledType(),
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'attributes': 'attributes_example',
        'date_created': '2013-10-20T19:20:30+01:00',
        'date_updated': '2013-10-20T19:20:30+01:00',
        'identity': 'identity_example',
        'messaging_binding_address': 'messaging_binding_address_example',
        'messaging_binding_projected_address': 'messaging_binding_projected_address_example',
        'messaging_binding_proxy_address': 'messaging_binding_proxy_address_example',
        'role_sid': 'role_sid_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Participants'.format(chat_service_sid='chat_service_sid_example', conversation_sid='conversation_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_conversation_participant(client):
    """Test case for delete_conversation_participant

    
    """
    headers = { 
        'x_twilio_webhook_enabled': openapi_server.ConversationParticipantEnumWebhookEnabledType(),
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/Conversations/{conversation_sid}/Participants/{sid}'.format(conversation_sid='conversation_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_service_conversation_participant(client):
    """Test case for delete_service_conversation_participant

    
    """
    headers = { 
        'x_twilio_webhook_enabled': openapi_server.ServiceConversationParticipantEnumWebhookEnabledType(),
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Participants/{sid}'.format(chat_service_sid='chat_service_sid_example', conversation_sid='conversation_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_conversation_participant(client):
    """Test case for fetch_conversation_participant

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Conversations/{conversation_sid}/Participants/{sid}'.format(conversation_sid='conversation_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_service_conversation_participant(client):
    """Test case for fetch_service_conversation_participant

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Participants/{sid}'.format(chat_service_sid='chat_service_sid_example', conversation_sid='conversation_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_conversation_participant(client):
    """Test case for list_conversation_participant

    
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
        path='/v1/Conversations/{conversation_sid}/Participants'.format(conversation_sid='conversation_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_service_conversation_participant(client):
    """Test case for list_service_conversation_participant

    
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
        path='/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Participants'.format(chat_service_sid='chat_service_sid_example', conversation_sid='conversation_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_conversation_participant(client):
    """Test case for update_conversation_participant

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'x_twilio_webhook_enabled': openapi_server.ConversationParticipantEnumWebhookEnabledType(),
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'attributes': 'attributes_example',
        'date_created': '2013-10-20T19:20:30+01:00',
        'date_updated': '2013-10-20T19:20:30+01:00',
        'identity': 'identity_example',
        'last_read_message_index': 56,
        'last_read_timestamp': 'last_read_timestamp_example',
        'messaging_binding_projected_address': 'messaging_binding_projected_address_example',
        'messaging_binding_proxy_address': 'messaging_binding_proxy_address_example',
        'role_sid': 'role_sid_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Conversations/{conversation_sid}/Participants/{sid}'.format(conversation_sid='conversation_sid_example', sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_service_conversation_participant(client):
    """Test case for update_service_conversation_participant

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'x_twilio_webhook_enabled': openapi_server.ServiceConversationParticipantEnumWebhookEnabledType(),
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'attributes': 'attributes_example',
        'date_created': '2013-10-20T19:20:30+01:00',
        'date_updated': '2013-10-20T19:20:30+01:00',
        'identity': 'identity_example',
        'last_read_message_index': 56,
        'last_read_timestamp': 'last_read_timestamp_example',
        'messaging_binding_projected_address': 'messaging_binding_projected_address_example',
        'messaging_binding_proxy_address': 'messaging_binding_proxy_address_example',
        'role_sid': 'role_sid_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Participants/{sid}'.format(chat_service_sid='chat_service_sid_example', conversation_sid='conversation_sid_example', sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


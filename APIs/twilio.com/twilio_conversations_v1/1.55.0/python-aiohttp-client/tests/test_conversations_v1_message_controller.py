# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.conversation_message_enum_order_type import ConversationMessageEnumOrderType
from openapi_server.models.conversation_message_enum_webhook_enabled_type import ConversationMessageEnumWebhookEnabledType
from openapi_server.models.conversations_v1_conversation_conversation_message import ConversationsV1ConversationConversationMessage
from openapi_server.models.conversations_v1_service_service_conversation_service_conversation_message import ConversationsV1ServiceServiceConversationServiceConversationMessage
from openapi_server.models.list_conversation_message_response import ListConversationMessageResponse
from openapi_server.models.list_service_conversation_message_response import ListServiceConversationMessageResponse
from openapi_server.models.service_conversation_message_enum_order_type import ServiceConversationMessageEnumOrderType
from openapi_server.models.service_conversation_message_enum_webhook_enabled_type import ServiceConversationMessageEnumWebhookEnabledType


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_conversation_message(client):
    """Test case for create_conversation_message

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'x_twilio_webhook_enabled': openapi_server.ConversationMessageEnumWebhookEnabledType(),
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'attributes': 'attributes_example',
        'author': 'author_example',
        'body': 'body_example',
        'content_sid': 'content_sid_example',
        'content_variables': 'content_variables_example',
        'date_created': '2013-10-20T19:20:30+01:00',
        'date_updated': '2013-10-20T19:20:30+01:00',
        'media_sid': 'media_sid_example',
        'subject': 'subject_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Conversations/{conversation_sid}/Messages'.format(conversation_sid='conversation_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_service_conversation_message(client):
    """Test case for create_service_conversation_message

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'x_twilio_webhook_enabled': openapi_server.ServiceConversationMessageEnumWebhookEnabledType(),
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'attributes': 'attributes_example',
        'author': 'author_example',
        'body': 'body_example',
        'content_sid': 'content_sid_example',
        'content_variables': 'content_variables_example',
        'date_created': '2013-10-20T19:20:30+01:00',
        'date_updated': '2013-10-20T19:20:30+01:00',
        'media_sid': 'media_sid_example',
        'subject': 'subject_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Messages'.format(chat_service_sid='chat_service_sid_example', conversation_sid='conversation_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_conversation_message(client):
    """Test case for delete_conversation_message

    
    """
    headers = { 
        'x_twilio_webhook_enabled': openapi_server.ConversationMessageEnumWebhookEnabledType(),
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/Conversations/{conversation_sid}/Messages/{sid}'.format(conversation_sid='conversation_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_service_conversation_message(client):
    """Test case for delete_service_conversation_message

    
    """
    headers = { 
        'x_twilio_webhook_enabled': openapi_server.ServiceConversationMessageEnumWebhookEnabledType(),
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Messages/{sid}'.format(chat_service_sid='chat_service_sid_example', conversation_sid='conversation_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_conversation_message(client):
    """Test case for fetch_conversation_message

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Conversations/{conversation_sid}/Messages/{sid}'.format(conversation_sid='conversation_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_service_conversation_message(client):
    """Test case for fetch_service_conversation_message

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Messages/{sid}'.format(chat_service_sid='chat_service_sid_example', conversation_sid='conversation_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_conversation_message(client):
    """Test case for list_conversation_message

    
    """
    params = [('Order', openapi_server.ConversationMessageEnumOrderType()),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Conversations/{conversation_sid}/Messages'.format(conversation_sid='conversation_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_service_conversation_message(client):
    """Test case for list_service_conversation_message

    
    """
    params = [('Order', openapi_server.ServiceConversationMessageEnumOrderType()),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Messages'.format(chat_service_sid='chat_service_sid_example', conversation_sid='conversation_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_conversation_message(client):
    """Test case for update_conversation_message

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'x_twilio_webhook_enabled': openapi_server.ConversationMessageEnumWebhookEnabledType(),
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'attributes': 'attributes_example',
        'author': 'author_example',
        'body': 'body_example',
        'date_created': '2013-10-20T19:20:30+01:00',
        'date_updated': '2013-10-20T19:20:30+01:00',
        'subject': 'subject_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Conversations/{conversation_sid}/Messages/{sid}'.format(conversation_sid='conversation_sid_example', sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_service_conversation_message(client):
    """Test case for update_service_conversation_message

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'x_twilio_webhook_enabled': openapi_server.ServiceConversationMessageEnumWebhookEnabledType(),
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'attributes': 'attributes_example',
        'author': 'author_example',
        'body': 'body_example',
        'date_created': '2013-10-20T19:20:30+01:00',
        'date_updated': '2013-10-20T19:20:30+01:00',
        'subject': 'subject_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Messages/{sid}'.format(chat_service_sid='chat_service_sid_example', conversation_sid='conversation_sid_example', sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


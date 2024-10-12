# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.configuration_webhook_enum_target import ConfigurationWebhookEnumTarget
from openapi_server.models.conversation_scoped_webhook_enum_method import ConversationScopedWebhookEnumMethod
from openapi_server.models.conversation_scoped_webhook_enum_target import ConversationScopedWebhookEnumTarget
from openapi_server.models.conversations_v1_configuration_configuration_webhook import ConversationsV1ConfigurationConfigurationWebhook
from openapi_server.models.conversations_v1_conversation_conversation_scoped_webhook import ConversationsV1ConversationConversationScopedWebhook
from openapi_server.models.conversations_v1_service_service_configuration_service_webhook_configuration import ConversationsV1ServiceServiceConfigurationServiceWebhookConfiguration
from openapi_server.models.conversations_v1_service_service_conversation_service_conversation_scoped_webhook import ConversationsV1ServiceServiceConversationServiceConversationScopedWebhook
from openapi_server.models.list_conversation_scoped_webhook_response import ListConversationScopedWebhookResponse
from openapi_server.models.list_service_conversation_scoped_webhook_response import ListServiceConversationScopedWebhookResponse
from openapi_server.models.service_conversation_scoped_webhook_enum_method import ServiceConversationScopedWebhookEnumMethod
from openapi_server.models.service_conversation_scoped_webhook_enum_target import ServiceConversationScopedWebhookEnumTarget


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_conversation_scoped_webhook(client):
    """Test case for create_conversation_scoped_webhook

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'configuration_filters': ['configuration_filters_example'],
        'configuration_flow_sid': 'configuration_flow_sid_example',
        'configuration_method': openapi_server.ConversationScopedWebhookEnumMethod(),
        'configuration_replay_after': 56,
        'configuration_triggers': ['configuration_triggers_example'],
        'configuration_url': 'configuration_url_example',
        'target': openapi_server.ConversationScopedWebhookEnumTarget()
        }
    response = await client.request(
        method='POST',
        path='/v1/Conversations/{conversation_sid}/Webhooks'.format(conversation_sid='conversation_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_service_conversation_scoped_webhook(client):
    """Test case for create_service_conversation_scoped_webhook

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'configuration_filters': ['configuration_filters_example'],
        'configuration_flow_sid': 'configuration_flow_sid_example',
        'configuration_method': openapi_server.ServiceConversationScopedWebhookEnumMethod(),
        'configuration_replay_after': 56,
        'configuration_triggers': ['configuration_triggers_example'],
        'configuration_url': 'configuration_url_example',
        'target': openapi_server.ServiceConversationScopedWebhookEnumTarget()
        }
    response = await client.request(
        method='POST',
        path='/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Webhooks'.format(chat_service_sid='chat_service_sid_example', conversation_sid='conversation_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_conversation_scoped_webhook(client):
    """Test case for delete_conversation_scoped_webhook

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/Conversations/{conversation_sid}/Webhooks/{sid}'.format(conversation_sid='conversation_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_service_conversation_scoped_webhook(client):
    """Test case for delete_service_conversation_scoped_webhook

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Webhooks/{sid}'.format(chat_service_sid='chat_service_sid_example', conversation_sid='conversation_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_configuration_webhook(client):
    """Test case for fetch_configuration_webhook

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Configuration/Webhooks',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_conversation_scoped_webhook(client):
    """Test case for fetch_conversation_scoped_webhook

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Conversations/{conversation_sid}/Webhooks/{sid}'.format(conversation_sid='conversation_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_service_conversation_scoped_webhook(client):
    """Test case for fetch_service_conversation_scoped_webhook

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Webhooks/{sid}'.format(chat_service_sid='chat_service_sid_example', conversation_sid='conversation_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_service_webhook_configuration(client):
    """Test case for fetch_service_webhook_configuration

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Services/{chat_service_sid}/Configuration/Webhooks'.format(chat_service_sid='chat_service_sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_conversation_scoped_webhook(client):
    """Test case for list_conversation_scoped_webhook

    
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
        path='/v1/Conversations/{conversation_sid}/Webhooks'.format(conversation_sid='conversation_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_service_conversation_scoped_webhook(client):
    """Test case for list_service_conversation_scoped_webhook

    
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
        path='/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Webhooks'.format(chat_service_sid='chat_service_sid_example', conversation_sid='conversation_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_configuration_webhook(client):
    """Test case for update_configuration_webhook

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'filters': ['filters_example'],
        'method': 'method_example',
        'post_webhook_url': 'post_webhook_url_example',
        'pre_webhook_url': 'pre_webhook_url_example',
        'target': openapi_server.ConfigurationWebhookEnumTarget()
        }
    response = await client.request(
        method='POST',
        path='/v1/Configuration/Webhooks',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_conversation_scoped_webhook(client):
    """Test case for update_conversation_scoped_webhook

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'configuration_filters': ['configuration_filters_example'],
        'configuration_flow_sid': 'configuration_flow_sid_example',
        'configuration_method': openapi_server.ConversationScopedWebhookEnumMethod(),
        'configuration_triggers': ['configuration_triggers_example'],
        'configuration_url': 'configuration_url_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Conversations/{conversation_sid}/Webhooks/{sid}'.format(conversation_sid='conversation_sid_example', sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_service_conversation_scoped_webhook(client):
    """Test case for update_service_conversation_scoped_webhook

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'configuration_filters': ['configuration_filters_example'],
        'configuration_flow_sid': 'configuration_flow_sid_example',
        'configuration_method': openapi_server.ServiceConversationScopedWebhookEnumMethod(),
        'configuration_triggers': ['configuration_triggers_example'],
        'configuration_url': 'configuration_url_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Webhooks/{sid}'.format(chat_service_sid='chat_service_sid_example', conversation_sid='conversation_sid_example', sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_service_webhook_configuration(client):
    """Test case for update_service_webhook_configuration

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'filters': ['filters_example'],
        'method': 'method_example',
        'post_webhook_url': 'post_webhook_url_example',
        'pre_webhook_url': 'pre_webhook_url_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Services/{chat_service_sid}/Configuration/Webhooks'.format(chat_service_sid='chat_service_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


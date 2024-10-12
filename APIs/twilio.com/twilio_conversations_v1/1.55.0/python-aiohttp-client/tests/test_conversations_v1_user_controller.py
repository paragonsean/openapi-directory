# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.conversations_v1_service_service_user import ConversationsV1ServiceServiceUser
from openapi_server.models.conversations_v1_user import ConversationsV1User
from openapi_server.models.list_service_user_response import ListServiceUserResponse
from openapi_server.models.list_user_response import ListUserResponse
from openapi_server.models.service_user_enum_webhook_enabled_type import ServiceUserEnumWebhookEnabledType
from openapi_server.models.user_enum_webhook_enabled_type import UserEnumWebhookEnabledType


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_service_user(client):
    """Test case for create_service_user

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'x_twilio_webhook_enabled': openapi_server.ServiceUserEnumWebhookEnabledType(),
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'attributes': 'attributes_example',
        'friendly_name': 'friendly_name_example',
        'identity': 'identity_example',
        'role_sid': 'role_sid_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Services/{chat_service_sid}/Users'.format(chat_service_sid='chat_service_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_user(client):
    """Test case for create_user

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'x_twilio_webhook_enabled': openapi_server.UserEnumWebhookEnabledType(),
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'attributes': 'attributes_example',
        'friendly_name': 'friendly_name_example',
        'identity': 'identity_example',
        'role_sid': 'role_sid_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Users',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_service_user(client):
    """Test case for delete_service_user

    
    """
    headers = { 
        'x_twilio_webhook_enabled': openapi_server.ServiceUserEnumWebhookEnabledType(),
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/Services/{chat_service_sid}/Users/{sid}'.format(chat_service_sid='chat_service_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_user(client):
    """Test case for delete_user

    
    """
    headers = { 
        'x_twilio_webhook_enabled': openapi_server.UserEnumWebhookEnabledType(),
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/Users/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_service_user(client):
    """Test case for fetch_service_user

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Services/{chat_service_sid}/Users/{sid}'.format(chat_service_sid='chat_service_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_user(client):
    """Test case for fetch_user

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Users/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_service_user(client):
    """Test case for list_service_user

    
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
        path='/v1/Services/{chat_service_sid}/Users'.format(chat_service_sid='chat_service_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_user(client):
    """Test case for list_user

    
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
        path='/v1/Users',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_service_user(client):
    """Test case for update_service_user

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'x_twilio_webhook_enabled': openapi_server.ServiceUserEnumWebhookEnabledType(),
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'attributes': 'attributes_example',
        'friendly_name': 'friendly_name_example',
        'role_sid': 'role_sid_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Services/{chat_service_sid}/Users/{sid}'.format(chat_service_sid='chat_service_sid_example', sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_user(client):
    """Test case for update_user

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'x_twilio_webhook_enabled': openapi_server.UserEnumWebhookEnabledType(),
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'attributes': 'attributes_example',
        'friendly_name': 'friendly_name_example',
        'role_sid': 'role_sid_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Users/{sid}'.format(sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


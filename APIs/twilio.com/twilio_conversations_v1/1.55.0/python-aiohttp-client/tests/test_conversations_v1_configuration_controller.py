# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.conversations_v1_configuration import ConversationsV1Configuration
from openapi_server.models.conversations_v1_service_service_configuration import ConversationsV1ServiceServiceConfiguration


pytestmark = pytest.mark.asyncio

async def test_fetch_configuration(client):
    """Test case for fetch_configuration

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Configuration',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_service_configuration(client):
    """Test case for fetch_service_configuration

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Services/{chat_service_sid}/Configuration'.format(chat_service_sid='chat_service_sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_configuration(client):
    """Test case for update_configuration

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'default_chat_service_sid': 'default_chat_service_sid_example',
        'default_closed_timer': 'default_closed_timer_example',
        'default_inactive_timer': 'default_inactive_timer_example',
        'default_messaging_service_sid': 'default_messaging_service_sid_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Configuration',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_service_configuration(client):
    """Test case for update_service_configuration

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'default_chat_service_role_sid': 'default_chat_service_role_sid_example',
        'default_conversation_creator_role_sid': 'default_conversation_creator_role_sid_example',
        'default_conversation_role_sid': 'default_conversation_role_sid_example',
        'reachability_enabled': True
        }
    response = await client.request(
        method='POST',
        path='/v1/Services/{chat_service_sid}/Configuration'.format(chat_service_sid='chat_service_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


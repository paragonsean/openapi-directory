# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.conversations_v1_service_service_configuration_service_notification import ConversationsV1ServiceServiceConfigurationServiceNotification


pytestmark = pytest.mark.asyncio

async def test_fetch_service_notification(client):
    """Test case for fetch_service_notification

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Services/{chat_service_sid}/Configuration/Notifications'.format(chat_service_sid='chat_service_sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_service_notification(client):
    """Test case for update_service_notification

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'added_to_conversation_enabled': True,
        'added_to_conversation_sound': 'added_to_conversation_sound_example',
        'added_to_conversation_template': 'added_to_conversation_template_example',
        'log_enabled': True,
        'new_message_badge_count_enabled': True,
        'new_message_enabled': True,
        'new_message_sound': 'new_message_sound_example',
        'new_message_template': 'new_message_template_example',
        'new_message_with_media_enabled': True,
        'new_message_with_media_template': 'new_message_with_media_template_example',
        'removed_from_conversation_enabled': True,
        'removed_from_conversation_sound': 'removed_from_conversation_sound_example',
        'removed_from_conversation_template': 'removed_from_conversation_template_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Services/{chat_service_sid}/Configuration/Notifications'.format(chat_service_sid='chat_service_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


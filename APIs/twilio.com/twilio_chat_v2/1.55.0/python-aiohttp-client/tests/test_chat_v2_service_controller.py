# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.chat_v2_service import ChatV2Service
from openapi_server.models.list_service_response import ListServiceResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_service(client):
    """Test case for create_service

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'friendly_name': 'friendly_name_example'
        }
    response = await client.request(
        method='POST',
        path='/v2/Services',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_service(client):
    """Test case for delete_service

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/Services/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_service(client):
    """Test case for fetch_service

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/Services/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_service(client):
    """Test case for list_service

    
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
        path='/v2/Services',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_service(client):
    """Test case for update_service

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'consumption_report_interval': 56,
        'default_channel_creator_role_sid': 'default_channel_creator_role_sid_example',
        'default_channel_role_sid': 'default_channel_role_sid_example',
        'default_service_role_sid': 'default_service_role_sid_example',
        'friendly_name': 'friendly_name_example',
        'limits_channel_members': 56,
        'limits_user_channels': 56,
        'media_compatibility_message': 'media_compatibility_message_example',
        'notifications_added_to_channel_enabled': True,
        'notifications_added_to_channel_sound': 'notifications_added_to_channel_sound_example',
        'notifications_added_to_channel_template': 'notifications_added_to_channel_template_example',
        'notifications_invited_to_channel_enabled': True,
        'notifications_invited_to_channel_sound': 'notifications_invited_to_channel_sound_example',
        'notifications_invited_to_channel_template': 'notifications_invited_to_channel_template_example',
        'notifications_log_enabled': True,
        'notifications_new_message_badge_count_enabled': True,
        'notifications_new_message_enabled': True,
        'notifications_new_message_sound': 'notifications_new_message_sound_example',
        'notifications_new_message_template': 'notifications_new_message_template_example',
        'notifications_removed_from_channel_enabled': True,
        'notifications_removed_from_channel_sound': 'notifications_removed_from_channel_sound_example',
        'notifications_removed_from_channel_template': 'notifications_removed_from_channel_template_example',
        'post_webhook_retry_count': 56,
        'post_webhook_url': 'post_webhook_url_example',
        'pre_webhook_retry_count': 56,
        'pre_webhook_url': 'pre_webhook_url_example',
        'reachability_enabled': True,
        'read_status_enabled': True,
        'typing_indicator_timeout': 56,
        'webhook_filters': ['webhook_filters_example'],
        'webhook_method': 'webhook_method_example'
        }
    response = await client.request(
        method='POST',
        path='/v2/Services/{sid}'.format(sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


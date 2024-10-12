# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.chat_v2_service_user_user_channel import ChatV2ServiceUserUserChannel
from openapi_server.models.list_user_channel_response import ListUserChannelResponse
from openapi_server.models.user_channel_enum_notification_level import UserChannelEnumNotificationLevel
from openapi_server.models.user_channel_enum_webhook_enabled_type import UserChannelEnumWebhookEnabledType


pytestmark = pytest.mark.asyncio

async def test_delete_user_channel(client):
    """Test case for delete_user_channel

    
    """
    headers = { 
        'x_twilio_webhook_enabled': openapi_server.UserChannelEnumWebhookEnabledType(),
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/Services/{service_sid}/Users/{user_sid}/Channels/{channel_sid}'.format(service_sid='service_sid_example', user_sid='user_sid_example', channel_sid='channel_sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_user_channel(client):
    """Test case for fetch_user_channel

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/Services/{service_sid}/Users/{user_sid}/Channels/{channel_sid}'.format(service_sid='service_sid_example', user_sid='user_sid_example', channel_sid='channel_sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_user_channel(client):
    """Test case for list_user_channel

    
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
        path='/v2/Services/{service_sid}/Users/{user_sid}/Channels'.format(service_sid='service_sid_example', user_sid='user_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_user_channel(client):
    """Test case for update_user_channel

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'last_consumed_message_index': 56,
        'last_consumption_timestamp': '2013-10-20T19:20:30+01:00',
        'notification_level': openapi_server.UserChannelEnumNotificationLevel()
        }
    response = await client.request(
        method='POST',
        path='/v2/Services/{service_sid}/Users/{user_sid}/Channels/{channel_sid}'.format(service_sid='service_sid_example', user_sid='user_sid_example', channel_sid='channel_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


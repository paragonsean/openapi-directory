# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.channel_webhook_enum_method import ChannelWebhookEnumMethod
from openapi_server.models.channel_webhook_enum_type import ChannelWebhookEnumType
from openapi_server.models.chat_v2_service_channel_channel_webhook import ChatV2ServiceChannelChannelWebhook
from openapi_server.models.list_channel_webhook_response import ListChannelWebhookResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_channel_webhook(client):
    """Test case for create_channel_webhook

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'configuration_filters': ['configuration_filters_example'],
        'configuration_flow_sid': 'configuration_flow_sid_example',
        'configuration_method': openapi_server.ChannelWebhookEnumMethod(),
        'configuration_retry_count': 56,
        'configuration_triggers': ['configuration_triggers_example'],
        'configuration_url': 'configuration_url_example',
        'type': openapi_server.ChannelWebhookEnumType()
        }
    response = await client.request(
        method='POST',
        path='/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks'.format(service_sid='service_sid_example', channel_sid='channel_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_channel_webhook(client):
    """Test case for delete_channel_webhook

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks/{sid}'.format(service_sid='service_sid_example', channel_sid='channel_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_channel_webhook(client):
    """Test case for fetch_channel_webhook

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks/{sid}'.format(service_sid='service_sid_example', channel_sid='channel_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_channel_webhook(client):
    """Test case for list_channel_webhook

    
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
        path='/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks'.format(service_sid='service_sid_example', channel_sid='channel_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_channel_webhook(client):
    """Test case for update_channel_webhook

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'configuration_filters': ['configuration_filters_example'],
        'configuration_flow_sid': 'configuration_flow_sid_example',
        'configuration_method': openapi_server.ChannelWebhookEnumMethod(),
        'configuration_retry_count': 56,
        'configuration_triggers': ['configuration_triggers_example'],
        'configuration_url': 'configuration_url_example'
        }
    response = await client.request(
        method='POST',
        path='/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks/{sid}'.format(service_sid='service_sid_example', channel_sid='channel_sid_example', sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


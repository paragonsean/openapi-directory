# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.channel_enum_channel_type import ChannelEnumChannelType
from openapi_server.models.channel_enum_webhook_enabled_type import ChannelEnumWebhookEnabledType
from openapi_server.models.chat_v2_service_channel import ChatV2ServiceChannel
from openapi_server.models.list_channel_response import ListChannelResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_channel(client):
    """Test case for create_channel

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'x_twilio_webhook_enabled': openapi_server.ChannelEnumWebhookEnabledType(),
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'attributes': 'attributes_example',
        'created_by': 'created_by_example',
        'date_created': '2013-10-20T19:20:30+01:00',
        'date_updated': '2013-10-20T19:20:30+01:00',
        'friendly_name': 'friendly_name_example',
        'type': openapi_server.ChannelEnumChannelType(),
        'unique_name': 'unique_name_example'
        }
    response = await client.request(
        method='POST',
        path='/v2/Services/{service_sid}/Channels'.format(service_sid='service_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_channel(client):
    """Test case for delete_channel

    
    """
    headers = { 
        'x_twilio_webhook_enabled': openapi_server.ChannelEnumWebhookEnabledType(),
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/Services/{service_sid}/Channels/{sid}'.format(service_sid='service_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_channel(client):
    """Test case for fetch_channel

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/Services/{service_sid}/Channels/{sid}'.format(service_sid='service_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_channel(client):
    """Test case for list_channel

    
    """
    params = [('Type', [openapi_server.ChannelEnumChannelType()]),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/Services/{service_sid}/Channels'.format(service_sid='service_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_channel(client):
    """Test case for update_channel

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'x_twilio_webhook_enabled': openapi_server.ChannelEnumWebhookEnabledType(),
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'attributes': 'attributes_example',
        'created_by': 'created_by_example',
        'date_created': '2013-10-20T19:20:30+01:00',
        'date_updated': '2013-10-20T19:20:30+01:00',
        'friendly_name': 'friendly_name_example',
        'unique_name': 'unique_name_example'
        }
    response = await client.request(
        method='POST',
        path='/v2/Services/{service_sid}/Channels/{sid}'.format(service_sid='service_sid_example', sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


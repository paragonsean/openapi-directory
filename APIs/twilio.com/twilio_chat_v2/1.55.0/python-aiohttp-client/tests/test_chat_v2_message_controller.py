# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.chat_v2_service_channel_message import ChatV2ServiceChannelMessage
from openapi_server.models.list_message_response import ListMessageResponse
from openapi_server.models.message_enum_order_type import MessageEnumOrderType
from openapi_server.models.message_enum_webhook_enabled_type import MessageEnumWebhookEnabledType


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_message(client):
    """Test case for create_message

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'x_twilio_webhook_enabled': openapi_server.MessageEnumWebhookEnabledType(),
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'attributes': 'attributes_example',
        'body': 'body_example',
        'date_created': '2013-10-20T19:20:30+01:00',
        'date_updated': '2013-10-20T19:20:30+01:00',
        '_from': '_from_example',
        'last_updated_by': 'last_updated_by_example',
        'media_sid': 'media_sid_example'
        }
    response = await client.request(
        method='POST',
        path='/v2/Services/{service_sid}/Channels/{channel_sid}/Messages'.format(service_sid='service_sid_example', channel_sid='channel_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_message(client):
    """Test case for delete_message

    
    """
    headers = { 
        'x_twilio_webhook_enabled': openapi_server.MessageEnumWebhookEnabledType(),
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}'.format(service_sid='service_sid_example', channel_sid='channel_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_message(client):
    """Test case for fetch_message

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}'.format(service_sid='service_sid_example', channel_sid='channel_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_message(client):
    """Test case for list_message

    
    """
    params = [('Order', openapi_server.MessageEnumOrderType()),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/Services/{service_sid}/Channels/{channel_sid}/Messages'.format(service_sid='service_sid_example', channel_sid='channel_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_message(client):
    """Test case for update_message

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'x_twilio_webhook_enabled': openapi_server.MessageEnumWebhookEnabledType(),
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'attributes': 'attributes_example',
        'body': 'body_example',
        'date_created': '2013-10-20T19:20:30+01:00',
        'date_updated': '2013-10-20T19:20:30+01:00',
        '_from': '_from_example',
        'last_updated_by': 'last_updated_by_example'
        }
    response = await client.request(
        method='POST',
        path='/v2/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}'.format(service_sid='service_sid_example', channel_sid='channel_sid_example', sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.chat_v1_service_channel_message import ChatV1ServiceChannelMessage
from openapi_server.models.list_message_response import ListMessageResponse
from openapi_server.models.message_enum_order_type import MessageEnumOrderType


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_message(client):
    """Test case for create_message

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'attributes': 'attributes_example',
        'body': 'body_example',
        '_from': '_from_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Services/{service_sid}/Channels/{channel_sid}/Messages'.format(service_sid='service_sid_example', channel_sid='channel_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_message(client):
    """Test case for delete_message

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}'.format(service_sid='service_sid_example', channel_sid='channel_sid_example', sid='sid_example'),
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
        path='/v1/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}'.format(service_sid='service_sid_example', channel_sid='channel_sid_example', sid='sid_example'),
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
        path='/v1/Services/{service_sid}/Channels/{channel_sid}/Messages'.format(service_sid='service_sid_example', channel_sid='channel_sid_example'),
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
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'attributes': 'attributes_example',
        'body': 'body_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}'.format(service_sid='service_sid_example', channel_sid='channel_sid_example', sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


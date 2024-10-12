# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.flex_v1_web_channel import FlexV1WebChannel
from openapi_server.models.list_web_channel_response import ListWebChannelResponse
from openapi_server.models.web_channel_enum_chat_status import WebChannelEnumChatStatus


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_web_channel(client):
    """Test case for create_web_channel

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'chat_friendly_name': 'chat_friendly_name_example',
        'chat_unique_name': 'chat_unique_name_example',
        'customer_friendly_name': 'customer_friendly_name_example',
        'flex_flow_sid': 'flex_flow_sid_example',
        'identity': 'identity_example',
        'pre_engagement_data': 'pre_engagement_data_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/WebChannels',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_web_channel(client):
    """Test case for delete_web_channel

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/WebChannels/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_web_channel(client):
    """Test case for fetch_web_channel

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/WebChannels/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_web_channel(client):
    """Test case for list_web_channel

    
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
        path='/v1/WebChannels',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_web_channel(client):
    """Test case for update_web_channel

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'chat_status': openapi_server.WebChannelEnumChatStatus(),
        'post_engagement_data': 'post_engagement_data_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/WebChannels/{sid}'.format(sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


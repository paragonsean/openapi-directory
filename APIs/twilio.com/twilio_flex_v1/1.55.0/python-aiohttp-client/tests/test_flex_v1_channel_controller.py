# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.flex_v1_channel import FlexV1Channel
from openapi_server.models.list_channel_response import ListChannelResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_channel(client):
    """Test case for create_channel

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'chat_friendly_name': 'chat_friendly_name_example',
        'chat_unique_name': 'chat_unique_name_example',
        'chat_user_friendly_name': 'chat_user_friendly_name_example',
        'flex_flow_sid': 'flex_flow_sid_example',
        'identity': 'identity_example',
        'long_lived': True,
        'pre_engagement_data': 'pre_engagement_data_example',
        'target': 'target_example',
        'task_attributes': 'task_attributes_example',
        'task_sid': 'task_sid_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Channels',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_channel(client):
    """Test case for delete_channel

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/Channels/{sid}'.format(sid='sid_example'),
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
        path='/v1/Channels/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_channel(client):
    """Test case for list_channel

    
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
        path='/v1/Channels',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


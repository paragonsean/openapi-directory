# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bot_channel import BotChannel
from openapi_server.models.channel_response_list import ChannelResponseList
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_channels_create(client):
    """Test case for channels_create

    
    """
    parameters = {"properties":{"channelName":"channelName"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.BotService/botServices/{resource_name}/channels/{channel_name}'.format(resource_group_name='resource_group_name_example', resource_name='resource_name_example', channel_name='channel_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_channels_delete(client):
    """Test case for channels_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.BotService/botServices/{resource_name}/channels/{channel_name}'.format(resource_group_name='resource_group_name_example', resource_name='resource_name_example', channel_name='channel_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_channels_get(client):
    """Test case for channels_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.BotService/botServices/{resource_name}/channels/{channel_name}'.format(resource_group_name='resource_group_name_example', resource_name='resource_name_example', channel_name='channel_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_channels_list_by_resource_group(client):
    """Test case for channels_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.BotService/botServices/{resource_name}/channels'.format(resource_group_name='resource_group_name_example', resource_name='resource_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_channels_list_with_keys(client):
    """Test case for channels_list_with_keys

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.BotService/botServices/{resource_name}/channels/{channel_name}/listChannelWithKeys'.format(resource_group_name='resource_group_name_example', resource_name='resource_name_example', channel_name='channel_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_channels_update(client):
    """Test case for channels_update

    
    """
    parameters = {"properties":{"channelName":"channelName"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.BotService/botServices/{resource_name}/channels/{channel_name}'.format(resource_group_name='resource_group_name_example', resource_name='resource_name_example', channel_name='channel_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


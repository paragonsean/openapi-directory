# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.channel_column import ChannelColumn
from openapi_server.models.channel_header import ChannelHeader
from openapi_server.models.channel_info import ChannelInfo
from openapi_server.models.channel_root_category import ChannelRootCategory


pytestmark = pytest.mark.asyncio

async def test_get_available_channels(client):
    """Test case for get_available_channels

    List all available channel for this store
    """
    params = [('storeId', '04730364-9826-4ff3-92e4-51fccd02bf10')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/channels/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_channel_categories(client):
    """Test case for get_channel_categories

    Get channel categories
    """
    headers = { 
        'Accept': 'application/json',
        'accept_encoding': ['accept_encoding_example'],
    }
    response = await client.request(
        method='GET',
        path='/v2/user/channels/{channel_id}/categories'.format(channel_id='2dc136a7-0d3d-4cc9-a825-a28a42c53e28'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_channel_columns(client):
    """Test case for get_channel_columns

    Get channel columns
    """
    body = ['body_example']
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept_encoding': ['accept_encoding_example'],
    }
    response = await client.request(
        method='POST',
        path='/v2/user/channels/{channel_id}/columns'.format(channel_id='2dc136a7-0d3d-4cc9-a825-a28a42c53e28'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_channel_info(client):
    """Test case for get_channel_info

    Get channel information
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/channels/{channel_id}'.format(channel_id='2dc136a7-0d3d-4cc9-a825-a28a42c53e28'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


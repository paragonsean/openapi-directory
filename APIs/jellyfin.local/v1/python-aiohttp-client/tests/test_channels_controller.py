# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.base_item_dto_query_result import BaseItemDtoQueryResult
from openapi_server.models.channel_features import ChannelFeatures
from openapi_server.models.item_fields import ItemFields
from openapi_server.models.item_filter import ItemFilter


pytestmark = pytest.mark.asyncio

async def test_get_all_channel_features(client):
    """Test case for get_all_channel_features

    Get all channel features.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Channels/Features',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_channel_features(client):
    """Test case for get_channel_features

    Get channel features.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Channels/{channel_id}/Features'.format(channel_id='channel_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_channel_items(client):
    """Test case for get_channel_items

    Get channel items.
    """
    params = [('folderId', 'folder_id_example'),
                    ('userId', 'user_id_example'),
                    ('startIndex', 56),
                    ('limit', 56),
                    ('sortOrder', 'sort_order_example'),
                    ('filters', [openapi_server.ItemFilter()]),
                    ('sortBy', 'sort_by_example'),
                    ('fields', [openapi_server.ItemFields()])]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Channels/{channel_id}/Items'.format(channel_id='channel_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_channels(client):
    """Test case for get_channels

    Gets available channels.
    """
    params = [('userId', 'user_id_example'),
                    ('startIndex', 56),
                    ('limit', 56),
                    ('supportsLatestItems', True),
                    ('supportsMediaDeletion', True),
                    ('isFavorite', True)]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Channels',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_latest_channel_items(client):
    """Test case for get_latest_channel_items

    Gets latest channel items.
    """
    params = [('userId', 'user_id_example'),
                    ('startIndex', 56),
                    ('limit', 56),
                    ('filters', [openapi_server.ItemFilter()]),
                    ('fields', [openapi_server.ItemFields()]),
                    ('channelIds', ['channel_ids_example'])]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Channels/Items/Latest',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


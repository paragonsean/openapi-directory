# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.channel import Channel
from openapi_server.models.create_channel_request import CreateChannelRequest
from openapi_server.models.edit_channel_request import EditChannelRequest
from openapi_server.models.legacy_error import LegacyError


pytestmark = pytest.mark.asyncio

async def test_create_channel(client):
    """Test case for create_channel

    Create a channel
    """
    body = openapi_server.CreateChannelRequest()
    headers = { 
        'Accept': 'application/vnd.vimeo.channel+json',
        'Content-Type': 'application/vnd.vimeo.channel+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/channels',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_channel(client):
    """Test case for delete_channel

    Delete a channel
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/channels/{channel_id}'.format(channel_id=927),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_edit_channel(client):
    """Test case for edit_channel

    Edit a channel
    """
    body = openapi_server.EditChannelRequest()
    headers = { 
        'Accept': 'application/vnd.vimeo.channel+json',
        'Content-Type': 'application/vnd.vimeo.channel+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/channels/{channel_id}'.format(channel_id=927),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_channel(client):
    """Test case for get_channel

    Get a specific channel
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.channel+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/channels/{channel_id}'.format(channel_id=927),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_channel_subscriptions(client):
    """Test case for get_channel_subscriptions

    Get all the channels to which a user subscribes
    """
    params = [('direction', 'asc'),
                    ('filter', 'filter_example'),
                    ('page', 1),
                    ('per_page', 10),
                    ('query', 'Stop motion'),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/vnd.vimeo.channel+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/users/{user_id}/channels'.format(user_id=152184),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_channel_subscriptions_alt1(client):
    """Test case for get_channel_subscriptions_alt1

    Get all the channels to which a user subscribes
    """
    params = [('direction', 'asc'),
                    ('filter', 'filter_example'),
                    ('page', 1),
                    ('per_page', 10),
                    ('query', 'Stop motion'),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/vnd.vimeo.channel+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/me/channels',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_channels(client):
    """Test case for get_channels

    Get all channels
    """
    params = [('direction', 'asc'),
                    ('filter', 'filter_example'),
                    ('page', 1),
                    ('per_page', 10),
                    ('query', 'Stop motion'),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/vnd.vimeo.channel+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/channels',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


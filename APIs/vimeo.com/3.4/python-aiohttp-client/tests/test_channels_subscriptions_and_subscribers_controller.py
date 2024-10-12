# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.legacy_error import LegacyError
from openapi_server.models.user import User


pytestmark = pytest.mark.asyncio

async def test_check_if_user_subscribed_to_channel(client):
    """Test case for check_if_user_subscribed_to_channel

    Check if a user follows a channel
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/users/{user_id}/channels/{channel_id}'.format(channel_id=927, user_id=152184),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_check_if_user_subscribed_to_channel_alt1(client):
    """Test case for check_if_user_subscribed_to_channel_alt1

    Check if a user follows a channel
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/me/channels/{channel_id}'.format(channel_id=927),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_channel_subscribers(client):
    """Test case for get_channel_subscribers

    Get all the followers of a channel
    """
    params = [('direction', 'asc'),
                    ('filter', 'filter_example'),
                    ('page', 1),
                    ('per_page', 10),
                    ('query', 'Stop motion'),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/vnd.vimeo.user+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/channels/{channel_id}/users'.format(channel_id=927),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscribe_to_channel(client):
    """Test case for subscribe_to_channel

    Subscribe a user to a specific channel
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/users/{user_id}/channels/{channel_id}'.format(channel_id=927, user_id=152184),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscribe_to_channel_alt1(client):
    """Test case for subscribe_to_channel_alt1

    Subscribe a user to a specific channel
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/me/channels/{channel_id}'.format(channel_id=927),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unsubscribe_from_channel(client):
    """Test case for unsubscribe_from_channel

    Unsubscribe a user from a specific channel
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/users/{user_id}/channels/{channel_id}'.format(channel_id=927, user_id=152184),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unsubscribe_from_channel_alt1(client):
    """Test case for unsubscribe_from_channel_alt1

    Unsubscribe a user from a specific channel
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/me/channels/{channel_id}'.format(channel_id=927),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


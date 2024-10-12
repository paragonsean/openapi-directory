# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_channel_moderators_request import AddChannelModeratorsRequest
from openapi_server.models.error import Error
from openapi_server.models.legacy_error import LegacyError
from openapi_server.models.remove_channel_moderators_request import RemoveChannelModeratorsRequest
from openapi_server.models.replace_channel_moderators_request import ReplaceChannelModeratorsRequest
from openapi_server.models.user import User


pytestmark = pytest.mark.asyncio

async def test_add_channel_moderator(client):
    """Test case for add_channel_moderator

    Add a specific channel moderator
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.user+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/channels/{channel_id}/moderators/{user_id}'.format(channel_id=927, user_id=152184),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_channel_moderators(client):
    """Test case for add_channel_moderators

    Add a list of channel moderators
    """
    body = openapi_server.AddChannelModeratorsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/channels/{channel_id}/moderators'.format(channel_id=927),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_channel_moderator(client):
    """Test case for get_channel_moderator

    Get a specific channel moderator
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.user+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/channels/{channel_id}/moderators/{user_id}'.format(channel_id=927, user_id=152184),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_channel_moderators(client):
    """Test case for get_channel_moderators

    Get all the moderators in a channel
    """
    params = [('direction', 'asc'),
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
        path='/channels/{channel_id}/moderators'.format(channel_id=927),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_channel_moderator(client):
    """Test case for remove_channel_moderator

    Remove a specific channel moderator
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.user+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/channels/{channel_id}/moderators/{user_id}'.format(channel_id=927, user_id=152184),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_channel_moderators(client):
    """Test case for remove_channel_moderators

    Remove a list of channel moderators
    """
    body = openapi_server.RemoveChannelModeratorsRequest()
    headers = { 
        'Accept': 'application/vnd.vimeo.user+json',
        'Content-Type': 'application/vnd.vimeo.user+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/channels/{channel_id}/moderators'.format(channel_id=927),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replace_channel_moderators(client):
    """Test case for replace_channel_moderators

    Replace the moderators of a channel
    """
    body = openapi_server.ReplaceChannelModeratorsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/channels/{channel_id}/moderators'.format(channel_id=927),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


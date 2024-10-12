# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.media_list_response import MediaListResponse
from openapi_server.models.user_response import UserResponse
from openapi_server.models.users_info_response import UsersInfoResponse


pytestmark = pytest.mark.asyncio

async def test_users_search_get(client):
    """Test case for users_search_get

    Search for a user by name.
    """
    params = [('q', 'q_example'),
                    ('count', 56)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/users/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_self_feed_get(client):
    """Test case for users_self_feed_get

    See the authenticated user's feed.
    """
    params = [('count', 56),
                    ('min_id', 'min_id_example'),
                    ('max_id', 'max_id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/users/self/feed',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_self_media_liked_get(client):
    """Test case for users_self_media_liked_get

    See the list of media liked by the authenticated user.
    """
    params = [('count', 56),
                    ('max_like_id', 'max_like_id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/users/self/media/liked',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_user_id_get(client):
    """Test case for users_user_id_get

    Get basic information about a user.
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/users/{user_id}'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_user_id_media_recent_get(client):
    """Test case for users_user_id_media_recent_get

    Get the most recent media published by a user.
    """
    params = [('count', 56),
                    ('max_timestamp', 56),
                    ('min_timestamp', 56),
                    ('min_id', 'min_id_example'),
                    ('max_id', 'max_id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/users/{user_id}/media/recent'.format(user_id='user_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


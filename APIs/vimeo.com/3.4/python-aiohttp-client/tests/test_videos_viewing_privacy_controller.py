# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.legacy_error import LegacyError
from openapi_server.models.user import User


pytestmark = pytest.mark.asyncio

async def test_add_video_privacy_user(client):
    """Test case for add_video_privacy_user

    Permit a specific user to view a private video
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.user+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/videos/{video_id}/privacy/users/{user_id}'.format(user_id=152184, video_id=258684937),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_video_privacy_users(client):
    """Test case for add_video_privacy_users

    Permit a list of users to view a private video
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.user+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/videos/{video_id}/privacy/users'.format(video_id=258684937),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_video_privacy_users_alt1(client):
    """Test case for add_video_privacy_users_alt1

    Permit a list of users to view a private video
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.user+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/channels/{channel_id}/videos/{video_id}/privacy/users'.format(channel_id=927, video_id=258684937),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_video_privacy_user(client):
    """Test case for delete_video_privacy_user

    Restrict a user from viewing a private video
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/videos/{video_id}/privacy/users/{user_id}'.format(user_id=152184, video_id=258684937),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_video_privacy_users(client):
    """Test case for get_video_privacy_users

    Get all the users who can view a user's private videos by default
    """
    params = [('page', 1),
                    ('per_page', 10)]
    headers = { 
        'Accept': 'application/vnd.vimeo.user+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/videos/{video_id}/privacy/users'.format(video_id=258684937),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_video_privacy_users_alt1(client):
    """Test case for get_video_privacy_users_alt1

    Get all the users who can view a user's private videos by default
    """
    params = [('page', 1),
                    ('per_page', 10)]
    headers = { 
        'Accept': 'application/vnd.vimeo.user+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/channels/{channel_id}/videos/{video_id}/privacy/users'.format(channel_id=927, video_id=258684937),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.set_channel_privacy_users_request import SetChannelPrivacyUsersRequest
from openapi_server.models.user import User


pytestmark = pytest.mark.asyncio

async def test_delete_channel_privacy_user(client):
    """Test case for delete_channel_privacy_user

    Restrict a user from viewing a private channel
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/channels/{channel_id}/privacy/users/{user_id}'.format(channel_id=927, user_id=152184),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_channel_privacy_users(client):
    """Test case for get_channel_privacy_users

    Get all the users who can view a private channel
    """
    params = [('direction', 'asc'),
                    ('page', 1),
                    ('per_page', 10)]
    headers = { 
        'Accept': 'application/vnd.vimeo.user+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/channels/{channel_id}/privacy/users'.format(channel_id=927),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_channel_privacy_user(client):
    """Test case for set_channel_privacy_user

    Permit a specific user to view a private channel
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/channels/{channel_id}/privacy/users/{user_id}'.format(channel_id=927, user_id=152184),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_channel_privacy_users(client):
    """Test case for set_channel_privacy_users

    Permit a list of users to view a private channel
    """
    body = openapi_server.SetChannelPrivacyUsersRequest()
    headers = { 
        'Accept': 'application/vnd.vimeo.user+json',
        'Content-Type': 'application/vnd.vimeo.user+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/channels/{channel_id}/privacy/users'.format(channel_id=927),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


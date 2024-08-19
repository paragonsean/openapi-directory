# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.relationship_post_response import RelationshipPostResponse
from openapi_server.models.relationship_response import RelationshipResponse
from openapi_server.models.users_info_response import UsersInfoResponse
from openapi_server.models.users_paging_response import UsersPagingResponse


pytestmark = pytest.mark.asyncio

async def test_users_self_requested_by_get(client):
    """Test case for users_self_requested_by_get

    List the users who have requested this user's permission to follow.
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/users/self/requested-by',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_user_id_followed_by_get(client):
    """Test case for users_user_id_followed_by_get

    Get the list of users this user is followed by.
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/users/{user_id}/followed-by'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_user_id_follows_get(client):
    """Test case for users_user_id_follows_get

    Get the list of users this user follows.
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/users/{user_id}/follows'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_user_id_relationship_get(client):
    """Test case for users_user_id_relationship_get

    Get information about a relationship to another user.
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/users/{user_id}/relationship'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_user_id_relationship_post(client):
    """Test case for users_user_id_relationship_post

    Modify the relationship between the current user and the target user.
    """
    params = [('action', 'action_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/users/{user_id}/relationship'.format(user_id='user_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


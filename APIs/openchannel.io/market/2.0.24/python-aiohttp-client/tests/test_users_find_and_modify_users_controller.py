# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.user import User
from openapi_server.models.user_pages import UserPages


pytestmark = pytest.mark.asyncio

async def test_users_get(client):
    """Test case for users_get

    Returns a paginated list of users
    """
    params = [('query', 'query_example'),
                    ('sort', 'sort_example'),
                    ('pageNumber', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/users',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_user_id_delete(client):
    """Test case for users_user_id_delete

    Removes a single user
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/users/{user_id}'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_user_id_get(client):
    """Test case for users_user_id_get

    Return a single user
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/users/{user_id}'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_user_id_patch(client):
    """Test case for users_user_id_patch

    Updates user fields
    """
    params = [('type', 'type_example'),
                    ('email', 'email_example'),
                    ('username', 'username_example'),
                    ('name', 'name_example'),
                    ('customData', 'custom_data_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PATCH',
        path='/v2/users/{user_id}'.format(user_id='user_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_user_id_post(client):
    """Test case for users_user_id_post

    Updates a single user or adds the user if they don't exist
    """
    params = [('type', 'type_example'),
                    ('email', 'email_example'),
                    ('username', 'username_example'),
                    ('name', 'name_example'),
                    ('customData', 'custom_data_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/users/{user_id}'.format(user_id='user_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.group_user_entity import GroupUserEntity


pytestmark = pytest.mark.asyncio

async def test_delete_group_users_id(client):
    """Test case for delete_group_users_id

    Delete Group User
    """
    params = [('group_id', 56),
                    ('user_id', 56)]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/rest/v1/group_users/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_group_users(client):
    """Test case for get_group_users

    List Group Users
    """
    params = [('user_id', 56),
                    ('cursor', 'cursor_example'),
                    ('per_page', 56),
                    ('group_id', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/group_users',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_patch_group_users_id(client):
    """Test case for patch_group_users_id

    Update Group User
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('admin', True)
    data.add_field('group_id', 56)
    data.add_field('user_id', 56)
    response = await client.request(
        method='PATCH',
        path='/api/rest/v1/group_users/{id}'.format(id=56),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_post_group_users(client):
    """Test case for post_group_users

    Create Group User
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('admin', True)
    data.add_field('group_id', 56)
    data.add_field('user_id', 56)
    response = await client.request(
        method='POST',
        path='/api/rest/v1/group_users',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.lock_entity import LockEntity


pytestmark = pytest.mark.asyncio

async def test_delete_locks_path(client):
    """Test case for delete_locks_path

    Delete Lock
    """
    params = [('token', 'token_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/rest/v1/locks/{path}'.format(path='path_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lock_list_for_path(client):
    """Test case for lock_list_for_path

    List Locks by path
    """
    params = [('cursor', 'cursor_example'),
                    ('per_page', 56),
                    ('include_children', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/locks/{path}'.format(path='path_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_post_locks_path(client):
    """Test case for post_locks_path

    Create Lock
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('allow_access_by_any_user', True)
    data.add_field('exclusive', True)
    data.add_field('recursive', 'recursive_example')
    data.add_field('timeout', 56)
    response = await client.request(
        method='POST',
        path='/api/rest/v1/locks/{path}'.format(path='path_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


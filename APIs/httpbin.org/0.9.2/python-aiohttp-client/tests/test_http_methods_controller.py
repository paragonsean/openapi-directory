# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_delete_delete(client):
    """Test case for delete_delete

    The request's DELETE parameters.
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/delete',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_get(client):
    """Test case for get_get

    The request's query parameters.
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/get',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_patch(client):
    """Test case for patch_patch

    The request's PATCH parameters.
    """
    headers = { 
    }
    response = await client.request(
        method='PATCH',
        path='/patch',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_post(client):
    """Test case for post_post

    The request's POST parameters.
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/post',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_put(client):
    """Test case for put_put

    The request's PUT parameters.
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/put',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


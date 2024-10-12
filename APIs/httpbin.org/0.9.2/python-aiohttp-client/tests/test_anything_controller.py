# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_anything_anything_delete(client):
    """Test case for anything_anything_delete

    Returns anything passed in request data.
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/anything/{anything}'.format(anything='anything_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_anything_anything_get(client):
    """Test case for anything_anything_get

    Returns anything passed in request data.
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/anything/{anything}'.format(anything='anything_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_anything_anything_patch(client):
    """Test case for anything_anything_patch

    Returns anything passed in request data.
    """
    headers = { 
    }
    response = await client.request(
        method='PATCH',
        path='/anything/{anything}'.format(anything='anything_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_anything_anything_post(client):
    """Test case for anything_anything_post

    Returns anything passed in request data.
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/anything/{anything}'.format(anything='anything_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_anything_anything_put(client):
    """Test case for anything_anything_put

    Returns anything passed in request data.
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/anything/{anything}'.format(anything='anything_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_anything_anything_trace(client):
    """Test case for anything_anything_trace

    Returns anything passed in request data.
    """
    headers = { 
    }
    response = await client.request(
        method='TRACE',
        path='/anything/{anything}'.format(anything='anything_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_anything_delete(client):
    """Test case for anything_delete

    Returns anything passed in request data.
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/anything',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_anything_get(client):
    """Test case for anything_get

    Returns anything passed in request data.
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/anything',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_anything_patch(client):
    """Test case for anything_patch

    Returns anything passed in request data.
    """
    headers = { 
    }
    response = await client.request(
        method='PATCH',
        path='/anything',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_anything_post(client):
    """Test case for anything_post

    Returns anything passed in request data.
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/anything',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_anything_put(client):
    """Test case for anything_put

    Returns anything passed in request data.
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/anything',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_anything_trace(client):
    """Test case for anything_trace

    Returns anything passed in request data.
    """
    headers = { 
    }
    response = await client.request(
        method='TRACE',
        path='/anything',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.doc import Doc


pytestmark = pytest.mark.asyncio

async def test_create_doc(client):
    """Test case for create_doc

    Create doc
    """
    body = {"hidden":True,"parentDoc":"parentDoc","body":"body","category":"category","title":"title","type":"basic"}
    headers = { 
        'Content-Type': 'application/json',
        'x_readme_version': 'v3.0',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/docs',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_doc(client):
    """Test case for delete_doc

    Delete doc
    """
    headers = { 
        'x_readme_version': 'v3.0',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/docs/{slug}'.format(slug='new-features'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_doc(client):
    """Test case for get_doc

    Get doc
    """
    headers = { 
        'x_readme_version': 'v3.0',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/docs/{slug}'.format(slug='new-features'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_docs(client):
    """Test case for search_docs

    Search docs
    """
    params = [('search', 'search_example')]
    headers = { 
        'x_readme_version': 'v3.0',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/docs/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_doc(client):
    """Test case for update_doc

    Update doc
    """
    body = {"hidden":True,"parentDoc":"parentDoc","body":"body","category":"category","title":"title","type":"basic"}
    headers = { 
        'Content-Type': 'application/json',
        'x_readme_version': 'v3.0',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/docs/{slug}'.format(slug='new-features'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


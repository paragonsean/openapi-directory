# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.custom_page import CustomPage


pytestmark = pytest.mark.asyncio

async def test_create_custom_page(client):
    """Test case for create_custom_page

    Create custom page
    """
    body = {"hidden":True,"html":"html","body":"body","htmlmode":False,"title":"title"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/custompages',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_custom_page(client):
    """Test case for delete_custom_page

    Delete custom page
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/custompages/{slug}'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_custom_page(client):
    """Test case for get_custom_page

    Get custom page
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/custompages/{slug}'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_custom_pages(client):
    """Test case for get_custom_pages

    Get custom pages
    """
    params = [('perPage', 10),
                    ('page', 1)]
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/custompages',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_custom_page(client):
    """Test case for update_custom_page

    Update custom page
    """
    body = {"hidden":True,"html":"html","body":"body","htmlmode":False,"title":"title"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/custompages/{slug}'.format(slug='slug_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_category(client):
    """Test case for get_category

    Get category
    """
    headers = { 
        'x_readme_version': 'v3.0',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/categories/{slug}'.format(slug='getting-started'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_category_docs(client):
    """Test case for get_category_docs

    Get docs for category
    """
    headers = { 
        'x_readme_version': 'v3.0',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/categories/{slug}/docs'.format(slug='getting-started'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


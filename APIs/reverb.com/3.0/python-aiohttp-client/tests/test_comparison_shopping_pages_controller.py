# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_comparison_shopping_pages_find_get(client):
    """Test case for comparison_shopping_pages_find_get

    Show comparison shopping page
    """
    params = [('id', 'id_example'),
                    ('slug', 'slug_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/comparison_shopping_pages/find',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_comparison_shopping_pages_get(client):
    """Test case for comparison_shopping_pages_get

    Returns a set of comparison shopping pages based on the current params
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/comparison_shopping_pages',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_comparison_shopping_pages_id_get(client):
    """Test case for comparison_shopping_pages_id_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/comparison_shopping_pages/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_comparison_shopping_pages_id_listings_get(client):
    """Test case for comparison_shopping_pages_id_listings_get

    Return new or used listings for a comparison shopping page
    """
    params = [('condition', 'condition_example'),
                    ('page', 1),
                    ('per_page', 24),
                    ('offset', 56)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/comparison_shopping_pages/{id}/listings'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_comparison_shopping_pages_id_reviews_get(client):
    """Test case for comparison_shopping_pages_id_reviews_get

    View reviews of a comparison shopping page
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/comparison_shopping_pages/{id}/reviews'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


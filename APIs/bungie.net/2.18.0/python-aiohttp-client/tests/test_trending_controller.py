# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.trending_get_trending_categories200_response import TrendingGetTrendingCategories200Response
from openapi_server.models.trending_get_trending_category200_response import TrendingGetTrendingCategory200Response
from openapi_server.models.trending_get_trending_entry_detail200_response import TrendingGetTrendingEntryDetail200Response


pytestmark = pytest.mark.asyncio

async def test_trending_get_trending_categories(client):
    """Test case for trending_get_trending_categories

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Trending/Categories/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_trending_get_trending_category(client):
    """Test case for trending_get_trending_category

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Trending/Categories/{category_id}/{page_number}'.format(category_id='category_id_example', page_number=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_trending_get_trending_entry_detail(client):
    """Test case for trending_get_trending_entry_detail

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Trending/Details/{trending_entry_type}/{identifier}'.format(identifier='identifier_example', trending_entry_type=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


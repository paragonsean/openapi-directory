# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.category_list import CategoryList
from openapi_server.models.podcast_list import PodcastList
from openapi_server.models.single_category import SingleCategory


pytestmark = pytest.mark.asyncio

async def test_categories_category_id_get(client):
    """Test case for categories_category_id_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'partner_id': 'special-key',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/partner/categories/{category_id}'.format(category_id='category_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_categories_category_id_podcasts_get(client):
    """Test case for categories_category_id_podcasts_get

    
    """
    params = [('page', 'page_example'),
                    ('pageSize', 'page_size_example'),
                    ('order', 'order_example'),
                    ('filters', 'filters_example')]
    headers = { 
        'Accept': 'application/json',
        'partner_id': 'special-key',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/partner/categories/{category_id}/podcasts'.format(category_id='category_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_categories_get(client):
    """Test case for categories_get

    
    """
    params = [('pageSize', 'page_size_example'),
                    ('page', 'page_example')]
    headers = { 
        'Accept': 'application/json',
        'partner_id': 'special-key',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/partner/categories',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


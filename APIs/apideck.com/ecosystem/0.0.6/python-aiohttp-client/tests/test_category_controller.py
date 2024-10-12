# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_categories_response import GetCategoriesResponse
from openapi_server.models.get_category_response import GetCategoryResponse
from openapi_server.models.get_listings_response import GetListingsResponse


pytestmark = pytest.mark.asyncio

async def test_categories_all(client):
    """Test case for categories_all

    List categories
    """
    params = [('cursor', 'cursor_example'),
                    ('limit', 50)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ecosystems/{ecosystem_id}/categories'.format(ecosystem_id='ecosystem_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_categories_one(client):
    """Test case for categories_one

    Get category
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ecosystems/{ecosystem_id}/categories/{id}'.format(ecosystem_id='ecosystem_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_category_listings_all(client):
    """Test case for category_listings_all

    List category listings
    """
    params = [('cursor', 'cursor_example'),
                    ('limit', 50)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ecosystems/{ecosystem_id}/categories/{id}/listings'.format(ecosystem_id='ecosystem_id_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


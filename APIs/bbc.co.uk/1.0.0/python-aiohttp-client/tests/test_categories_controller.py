# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.categories_response import CategoriesResponse
from openapi_server.models.category_error_response import CategoryErrorResponse


pytestmark = pytest.mark.asyncio

async def test_categories_get(client):
    """Test case for categories_get

    List of categories
    """
    params = [('kind', 'kind_example')]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/categories',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_categories_id_get(client):
    """Test case for categories_id_get

    Category by ID
    """
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/categories/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


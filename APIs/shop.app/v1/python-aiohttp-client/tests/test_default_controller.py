# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.search_response import SearchResponse


pytestmark = pytest.mark.asyncio

async def test_details(client):
    """Test case for details

    Return more details about a list of products.
    """
    params = [('ids', 'ids_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/openai/details',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search(client):
    """Test case for search

    Search for products
    """
    params = [('query', 'query_example'),
                    ('price_min', 3.4),
                    ('price_max', 3.4),
                    ('similar_to_id', 'similar_to_id_example'),
                    ('num_results', 'num_results_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/openai/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.banners import Banners
from openapi_server.models.correction import Correction
from openapi_server.models.error import Error
from openapi_server.models.facets import Facets
from openapi_server.models.product_search import ProductSearch
from openapi_server.models.search_suggestions import SearchSuggestions


pytestmark = pytest.mark.asyncio

async def test_banners_facets_get(client):
    """Test case for banners_facets_get

    Get list of banners registered for query
    """
    params = [('query', 'query_example'),
                    ('locale', 'en-US')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/banners/{facets}'.format(facets='/'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_correction_search_get(client):
    """Test case for correction_search_get

    Get attempt of correction of a misspelled term
    """
    params = [('query', 'query_example'),
                    ('locale', 'en-US')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/correction_search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_facets_facets_get(client):
    """Test case for facets_facets_get

    Get list of the possible facets for a given query
    """
    params = [('query', 'query_example'),
                    ('locale', 'en-US'),
                    ('hideUnavailableItems', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/facets/{facets}'.format(facets='/'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_search_facets_get(client):
    """Test case for product_search_facets_get

    Get list of products for a query
    """
    params = [('query', 'query_example'),
                    ('simulationBehavior', default),
                    ('count', 24),
                    ('page', 1),
                    ('sort', 'sort_example'),
                    ('locale', 'en-US'),
                    ('hideUnavailableItems', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/product_search/{facets}'.format(facets='/'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_suggestions_get(client):
    """Test case for search_suggestions_get

    Get list of suggested terms similar to the search term
    """
    params = [('query', 'query_example'),
                    ('locale', 'en-US')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/search_suggestions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


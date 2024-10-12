# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.autocomplete_search_suggestions import AutocompleteSearchSuggestions
from openapi_server.models.error import Error
from openapi_server.models.top_searches import TopSearches


pytestmark = pytest.mark.asyncio

async def test_autocomplete_suggestions_get(client):
    """Test case for autocomplete_suggestions_get

    Get list of suggested terms and attributes similar to the search term
    """
    params = [('query', 'query_example'),
                    ('locale', 'en-US')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/autocomplete_suggestions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_top_searches_get(client):
    """Test case for top_searches_get

    Get list of the 10 most searched terms
    """
    params = [('locale', 'en-US')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/top_searches',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

